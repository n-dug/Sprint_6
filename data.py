class URL:
    SEARCH_DZEN_URL = 'https://dzen.ru/?yredirect=true'  # URL Яндекс.Дзен
    BASE_SCOOTER_URL = 'https://qa-scooter.praktikum-services.ru/'  # URL сервиса заказа самокатов


class AnswersList:  # Ответы в FAQ
    answers_text = [
            'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
            'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать '
            'несколько заказов — один за другим.',
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды '
            'начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, '
            'суточная аренда закончится 9 мая в 20:30.',
            'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
            'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
            'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без '
            'передышек и во сне. Зарядка не понадобится.',
            'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
            'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    ]


class Users:  # 2 набора данных
    user_1 = {
        1: 'Иван',
        2: 'Иванов',
        3: 'Москва, ул. Кирова, 87',
        4: 'Университет',
        5: '89522346600',
        6: '01.08.2024',
        7: 'Пойду кататься',
    }

    user_2 = {
        1: 'Михаил',
        2: 'Михайлов',
        3: 'Москва, Цветной бульвар, 1',
        4: 'Университет',
        5: '89287665556',
        6: '02.08.2024',
        7: 'Прошу выдать самокат',
    }
