
import requests

def send_message( 
    token:str, chat_id:int, 
    attack_count:int, data:list[list] 
)->None:
    
    text = get_text(attack_count, data)
    send_message_by_url( text=text, token=token,chat_id=chat_id)
    

def get_text(attack_count:int, data:list[list]) -> str:
    """
Пример входных данных:
[
    ['PortScan', '2024-06-06 22-55-54.807595+00-00'], 
    ['Что-то еще', '2024-06-06 22-55-54.810682+00-00'], 
    ['Dudos', '2024-06-06 22-55-54.810736+00-00']
]
    """
    if (attack_count < 1) or (len(data)<1):
        return "Все нормально"
    
    text = f"Было обнаруженно {attack_count} атак.\n"
    text += "\nБыли обнаружены следующие атаки:"
    temp = []
    for i in data:
        if i[0] not in temp:
            temp.append(i[0])
            text += f"\n{i[0]}"
    
    return text    
    
    
def send_message_by_url(text:str, token:str, chat_id:int) -> None:
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data).json()
