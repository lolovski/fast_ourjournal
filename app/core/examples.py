user_create_examples = {
                'middle_name': {
                    'summary': 'С отчеством',
                    'description': 'Отчество передается строкой',
                    'value': {
                        'username': 'admin',
                        'password': '<PASSWORD>',
                        'last_name': 'Иванов',
                        'first_name': 'Иван',
                        'middle_name': "Иванович",
                        'class_user': 1
                    }
                },
                'not_middle_name': {
                    'summary': 'Без отчества',
                    'description': 'Отчество не передается никак',
                    'value': {
                        'username': 'admin',
                        'password': '<PASSWORD>',
                        'last_name': 'Иванов',
                        'first_name': 'Иван',
                        'class_user': 1
                    }
                },

            }