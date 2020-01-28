'''
Código simples para baixar vídeos do youtube/facebook/instagram
'''
import webbrowser

url = input('URL: ')
download = 'savefrom.net/' + url
webbrowser.open(download)