import requests

topico = "livia"

url = f"https://ntfy.sh/{topico}"

requests.post(url, data = "Hello my friend, Livia".encode('utf-8'))

print ('mensagem enviada')