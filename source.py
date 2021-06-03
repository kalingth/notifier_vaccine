from requests import get, post, Session
from time import sleep
from tkinter import messagebox, Tk
from webbrowser import open as op

locais = { # Locais identificados por seus respectivos links.
    "https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_data/1":"Alto da Serra(Hipershopping)",
    "https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_data/2":"Bingen",
    "https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_data/3":"Centro(Benjamin Constant)",
    "https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_data/4":"Itaipava(Parque de Exposição)",
    "https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_data/5":"Itamarati(Clube Palmeiras)",
    "https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_data/6":"Correas",
    "https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_data/8":"Clube Petropolitano",
    "https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_data/9":"Posse",
    "https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_data/10":"Quitandinha",
    "https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_data/14":"Itaipava - Trab. Educação"
}


headers = { # Somente navegadores são aceitos, portanto, o cabeçalho simula um navegador.
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "max-age=0"
}

def success(manhaIdosos, tardeIdosos, manhaComorb, tardeComorb):
    """Função success:
    
    Apresentará uma notificação na tela e abrirá o site da secretaria de saúde para o usuário.
    """
    root = Tk()
    root.withdraw()
    mensagem = "Foram abertas as seguintes vagas:\n"
    mensagem += "\nManhã para idosos:\n" + '\n'.join(f"♦ {locais[k]}" for k in locais.keys() if k in manhaIdosos) + '\n'
    mensagem += "\nTarde para idosos:\n" + '\n'.join(f"♦ {locais[k]}" for k in locais.keys() if k in tardeIdosos) + '\n'
    mensagem += "\nManhã para pacientes com comorbidades:\n" + '\n'.join(f"♦ {locais[k]}" for k in locais.keys() if k in manhaComorb) + '\n'
    mensagem += "\nTarde para pacientes com comorbidades:\n" + '\n'.join(f"♦ {locais[k]}" for k in locais.keys() if k in tardeComorb) + '\n'
    op('https://smspetropolis.net.br/cadastrarVacina.html', new=0, autoraise=True)
    sleep(1)
    messagebox.showinfo("Vagas encontradas!!", mensagem)
    root.destroy()

def idosos():
    """Função idosos:
    
    Recuperará um Cookie de sessão onde este representará um idoso.
    Utilizando este Cookie, o programa distinguirá as vagas para idosos das vagas de pacientes com comorbidades.
    """
    headers = { "Host": "smspetropolis.net.br",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": "https://smspetropolis.net.br/agendarvacinacovid/home/inicio",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "60",
                "Origin": "https://smspetropolis.net.br",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache" }
    session = Session()
    session.post("https://smspetropolis.net.br/agendarvacinacovid/home/inicio", headers=headers,data="cpf=12345678901&datanasc=1960-01-01&idade=61&Submit=submit_p")
    cookie = session.cookies.get_dict()
    session.close()
    return "; ".join(f"{key}={value}" for key, value in cookie.items())

def comorbidades():
    """Função comorbidades:
    
    Recuperará um Cookie de sessão onde este representará um paciente portador de comorbidades.
    Utilizando este Cookie, o programa distinguirá as vagas para pacientes com comorbidades das vagas destinadas aos idosos.
    """
    headers = { "Host": "smspetropolis.net.br",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": "https://smspetropolis.net.br/agendarvacinacovid/home/inicio",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "60",
                "Origin": "https://smspetropolis.net.br",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache" }
    session = Session()
    session.post("https://smspetropolis.net.br/agendarvacinacovid/home/inicio", headers=headers,data="cpf=12345678901&datanasc=1970-01-01&idade=51&Submit=submit_p")
    cookie = session.cookies.get_dict()
    session.close()
    return "; ".join(f"{key}={value}" for key, value in cookie.items())


if __name__ == "__main__":                      # Método principal.
    while True:                                 # Chama um ciclo infinito que parará quando novas vagas forem encontradas.
        try:                                    # Cláusula try utilizada para caso ocorram erros de rede - tanto por parte do servidor quanto do cliente.
            headers["Cookie"] = idosos()        # Utiliza o método idosos para gerar o cookie de representação deste grupo
            im = get("https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_local/0", headers=headers).text # Idosos Manhã
            it = get("https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_local/9", headers=headers).text # Idosos Tarde
            headers["Cookie"] = comorbidades()  # Utiliza o método comorbidades para gerar o cookie de representação deste grupo
            cm = get("https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_local/0", headers=headers).text # Comorbidade Manhã
            ct = get("https://smspetropolis.net.br/agendarvacinacovid/home/selecionar_local/9", headers=headers).text # Comorbidade Tarde
        except:                                 # Caso ocorra um erro na rede, ele apenas reexecutará a rotina e ignorará o erro.
            continue
        if any((k in (im + it + cm + ct) for k in locais.keys())): # Checa se há vagas
            success(im, it, cm, ct)             # Se houverem vagas, ele irá chamar o método success para abrir o site da secretaria e notificar os locais disponíveis e os turnos
            break                               # Caso haja sucesso, irá para o ciclo.
        sleep(60)                               # Espera um minuto para tentar novamente
