def send_email(message, recipient,sender = "university.help@gmail.com"):
    if ("@" and (".com" or ".ru" or ".net")) not in (recipient or sender) or ("@" or (".com" or ".ru" or ".net")) not in (recipient or sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {recipient} на адрес {sender}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('messagje','urban.info@gmail.com','urban.fan@mail.ru')
send_email('messagje','urban.student@mail.ru','urban.teacher@mail.uk')
send_email('messagje','university.help@gmail.com')
