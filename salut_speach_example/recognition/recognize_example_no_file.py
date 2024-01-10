import requests
import uuid
import os
import grpc
import itertools
import pyaudio
import time
from typing import ByteString, Dict
from dotenv import load_dotenv

import recognition_pb2
import recognition_pb2_grpc


load_dotenv()


class SalutVoiceAssistant:

    CHUNK_SIZE = 2048
    SLEEP_TIME = 0.1

    ENCODING_PCM = 'pcm'

    ENCODINGS_MAP = {
        ENCODING_PCM: recognition_pb2.RecognitionOptions.PCM_S16LE,
        'opus': recognition_pb2.RecognitionOptions.OPUS,
        'mp3': recognition_pb2.RecognitionOptions.MP3,
        'flac': recognition_pb2.RecognitionOptions.FLAC,
        'alaw': recognition_pb2.RecognitionOptions.ALAW,
        'mulaw': recognition_pb2.RecognitionOptions.MULAW,
    }

    sample_format = pyaudio.paInt16
    channels = 1
    fs = 16000
    p = pyaudio.PyAudio()
    stream = p.open(
        format=sample_format,
        channels=channels,
        rate=fs,
        input=True,
        frames_per_buffer=CHUNK_SIZE
    )

    def __init__(self, auth_data):
        self.auth_data = auth_data
        self.access_token = self.get_bearer_token()
        self.stream.start_stream()

    def get_bearer_token(self):
        """
        Полученеи Bearer токена.
        """
        headers = {
            'Authorization': f'Basic {self.auth_data}',
            'RqUID': str(uuid.uuid4()),
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'scope': 'SALUTE_SPEECH_PERS',
        }
        response = requests.post(
            'https://ngw.devices.sberbank.ru:9443/api/v2/oauth',
            headers=headers,
            data=data,
            verify="../russian_trusted_root_ca.cer"
        )
        if response.status_code == 200:
            data = response.json()
            print(data)
            if 'access_token' in data:
                return data['access_token']

    @staticmethod
    def try_printing_request_id(md):
        for m in md:
            if m.key == 'x-request-id':
                print('RequestID:', m.value)

    def generate_audio_chunks(self, is_mic=True):
        if is_mic:
            return self.generate_audio_chunks_mic()
        return self.generate_audio_chunks_file()

    def generate_audio_chunks_mic(self):
        i = 0
        while True:
            time.sleep(self.SLEEP_TIME)
            i += 1
            data = self.stream.read(self.CHUNK_SIZE)
            print(data)
            yield recognition_pb2.RecognitionRequest(audio_chunk=data)

    def generate_audio_chunks_file(self):
        path = 'test.wav'
        with open(path, 'rb') as f:
            for data in iter(lambda: f.read(self.CHUNK_SIZE), b''):
                print(data)
                yield recognition_pb2.RecognitionRequest(audio_chunk=data)
                time.sleep(self.SLEEP_TIME)

    def voice_recognize(self):
        ssl_cred = grpc.ssl_channel_credentials(
            root_certificates=open('../russian_trusted_root_ca.cer', 'rb').read(),
        )
        token_cred = grpc.access_token_call_credentials(self.access_token)

        channel = grpc.secure_channel(
            os.environ.get('RECOGNIZE_HOST'),
            grpc.composite_channel_credentials(ssl_cred, token_cred)
        )

        stub = recognition_pb2_grpc.SmartSpeechStub(channel)

        metadata_pairs = []

        recognition_options = recognition_pb2.RecognitionOptions()
        setattr(recognition_options, 'audio_encoding', self.ENCODINGS_MAP.get(self.ENCODING_PCM))
        setattr(recognition_options, 'sample_rate', 16000)
        setattr(recognition_options, 'hypotheses_count', 1)
        setattr(recognition_options, 'channels_count', 1)

        con = stub.Recognize(itertools.chain(
            (recognition_pb2.RecognitionRequest(options=recognition_options),),
            self.generate_audio_chunks(),
        ), metadata=metadata_pairs)

        try:
            for resp in con:
                if not resp.eou:
                    print('Got partial result:')
                else:
                    print('Got end-of-utterance result:')

                for i, hyp in enumerate(resp.results):
                    print(
                        '  Hyp #{}: {}'.format(i + 1, hyp.text))

                """
                if resp.eou and args.emotions_result:
                    print('  Emotions: pos={}, neu={}, neg={}'.format(
                        resp.emotions_result.positive,
                        resp.emotions_result.neutral,
                        resp.emotions_result.negative,
                    ))                
                """

        except grpc.RpcError as err:
            print('RPC error: code = {}, details = {}'.format(err.code(), err.details()))
        except Exception as exc:
            print('Exception:', exc)
        else:
            print('Recognition has finished')
        finally:
            self.try_printing_request_id(con.initial_metadata())
            channel.close()


if __name__ == "__main__":

    voice_assistant = SalutVoiceAssistant(os.environ.get('AUTH_DATA'))
    # print(voice_assistant.access_token)
    # test_recognize(voice_assistant)
    voice_assistant.voice_recognize()