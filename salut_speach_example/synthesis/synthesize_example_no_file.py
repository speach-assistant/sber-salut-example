import requests
import uuid
import os
import grpc
from typing import ByteString, Dict
from dotenv import load_dotenv

import synthesis_pb2
import synthesis_pb2_grpc


load_dotenv()


class SalutVoiceAssistant:

    ENCODING_PCM = 'pcm'
    ENCODING_OPUS = 'opus'
    ENCODING_WAV = 'wav'
    ENCODINGS_MAP = {
        ENCODING_PCM: synthesis_pb2.SynthesisRequest.PCM_S16LE,
        ENCODING_OPUS: synthesis_pb2.SynthesisRequest.OPUS,
        ENCODING_WAV: synthesis_pb2.SynthesisRequest.WAV,
    }

    TYPE_TEXT = 'text'
    TYPE_SSML = 'ssml'
    TYPES_MAP = {
        TYPE_TEXT: synthesis_pb2.SynthesisRequest.TEXT,
        TYPE_SSML: synthesis_pb2.SynthesisRequest.SSML,
    }

    def __init__(self, auth_data):
        self.auth_data = auth_data
        self.access_token = self.get_bearer_token()

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

    def voice_synthesize(self, data: str) -> ByteString:
        ssl_cred = grpc.ssl_channel_credentials(
            root_certificates=open('../russian_trusted_root_ca.cer', 'rb').read(),
        )
        token_cred = grpc.access_token_call_credentials(self.access_token)

        channel = grpc.secure_channel(
            os.environ.get('SYNTHESIS_HOST'),
            grpc.composite_channel_credentials(ssl_cred, token_cred)
        )

        stub = synthesis_pb2_grpc.SmartSpeechStub(channel)

        synthesis_options = synthesis_pb2.SynthesisRequest()
        setattr(synthesis_options, 'text', data)
        setattr(synthesis_options, 'audio_encoding', self.ENCODINGS_MAP.get(self.ENCODING_WAV))
        setattr(synthesis_options, 'language', 'ru-RU')
        setattr(synthesis_options, 'voice', 'Bys_24000')

        con = stub.Synthesize(
            synthesis_options
        )

        result = b''

        try:
            for resp in con:
                result += resp.data
        except grpc.RpcError as err:
            print('RPC error: code = {}, details = {}'.format(err.code(), err.details()))
        except Exception as exc:
            print('Exception:', exc)
        else:
            print('Synthesis has finished')
        finally:
            self.try_printing_request_id(con.initial_metadata())
            channel.close()
            return result


def test_synthesize(va: SalutVoiceAssistant) -> None:
    import pyaudio
    import io
    import sounddevice as sd
    import soundfile as sf

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=24000,
                    output=True)

    text = "Привет человек, я робот Петрович."
    data = va.voice_synthesize(
        text
    )
    audio_data, samplerate = sf.read(io.BytesIO(data))
    sd.play(audio_data, samplerate)
    status = sd.wait()
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":

    voice_assistant = SalutVoiceAssistant(os.environ.get('AUTH_DATA'))
    # print(voice_assistant.access_token)
    # test_recognize(voice_assistant)
    test_synthesize(voice_assistant)