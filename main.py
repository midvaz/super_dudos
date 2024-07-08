import time
from datetime import datetime, timezone

from data_preproc import read_csv, preprocessor
from neural_check import neurol_check
from get_message import send_message
from config import unique_labels, model_path, dataset_path, TOKEN, ADMIS_ID


def create_logs(e:str) -> None:
    time_now = str(
            datetime.fromtimestamp(time.time(), timezone.utc) 
    ).replace(':','-')
        
    with open (f'./logs/{time_now}.txt', "x") as file:
        file.write(f"{e}")
        

def main() -> None:
    data = preprocessor(
        data = read_csv(filepath=dataset_path),
        stopor=100000
    )
    print("все ок")
    attack_list, attack_count = neurol_check(
        data=data,
        unique_labels=unique_labels,
        model_path=model_path
    )

    if attack_count > 0:
        for id in ADMIS_ID:
            send_message(
                token=TOKEN,
                chat_id=id,
                attack_count=attack_count,
                data=attack_list
            )
    
    
if __name__ == '__main__':
    now = time.time()
    main()
    print(f'{(time.time()-now)} минут')
    # time.sleep(300)
    # while True:
    #     try:
    #         now = time.time()
    #         main()
    #         print(f'{(time.time()-now)/60} минут')
    #         time.sleep(300)
    #     except Exception as e:
    #         print("Error: ", e)
    #         create_logs(e)
    #         time.sleep(15)