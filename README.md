# Shambles

Como criei o projeto

O python precisa de um ambiente virtual, então é necessário configura-lo

python -m venv env
Depois de criar o ambiente, precisa ativar ele

Voce vai indicar onde está o caminho do ambiente 2. env\Scripts\activate

Instalar as dependencias, achei um pouco estranho (kkk), o gerenciador de pacotes é um arquivo txt por nome requirements.txt pip
python-dotenv pytube
setuptools
tk

eu usei as versões abaixo pip 24.0 python-dotenv 1.0.1 pytube 15.0.0 setuptools 65.5.0 tk 0.1.0

pip install -r .\requirements.txt

para criar o .exe eu instalei a lib pyinstaller e executei o cmd abaixo:

cd src pyinstaller --onefile --windowed app.py

Ainda não está 100% funcional o .exe, pq eu não consegui resolver o problema do windows, o windows entende que o programa é um virus.