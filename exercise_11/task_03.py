# Создать классы, спецификации которых приведены ниже. Определить конструкторы .
# Определить дополнительно методы __str__. Определить дополнительно методы в классе, создающие массив объектов.
# Задать критерий выбора данных и вывести эти данные на консоль.
# Алексей
# Patient: id, Фамилия, Имя, Отчество, Адрес, Телефон, Номер ммедицинской карты, Диагноз.
# Создать массив объектов. Вывести:
#   a) список пациентов, имеющих данный диагноз;
#   b) список пациентов, номер медицинской карты которых находится в за- данном интервале.


class Patient:
    def __init__(self, _id: int, surname: str, name: str, patronymic: str, address: str, tel: str, card_num: int,
                 diagnosis: str):
        self.id = _id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.tel = tel
        self.card_num = card_num
        self.diagnosis = diagnosis

    def __str__(self):
        return "{} ({}) {} {} {} /{}/{}/{}".format(self.id, self.card_num, self.surname, self.name, self.patronymic,
                                                   self.address, self.tel, self.diagnosis)

    @staticmethod
    def create_from_tup(tuples: ()):
        patients = []
        ids = []
        for tup in tuples:
            if tup[0] in ids:
                print("У пациента не уникальный id: {}".format(tup))
                continue
            try:
                patient = Patient(*tup)
            except TypeError:
                print("Не получилось создать пациента по данным: {}".format(tup))
                continue
            patients.append(patient)
            ids.append(patient.id)
        return patients


class Pain:
    HEAD_ACHE = "HEADACHE"
    ORVI = "ORVI"
    NO_PAIN = ""


patientsTup = [
    (1, "Dobrov", "Aleksey", "Igorevich", "TGN", "+1234567", 1010, Pain.HEAD_ACHE),
    (2, "Zhukov", "Sergey", "Gaydarovich", "MSK", "+1234567", 1020, Pain.ORVI),
    (3, "Nilsky", "Oleg", "Slavovich", "RND", "+1234567", 1030, Pain.NO_PAIN),
    (4, "Staryh", "Vladimir", "Sergeevich", "KRD", "+1234567", 1040, Pain.HEAD_ACHE),
    (5, "Belov", "Vladimir", "Nikolaevich", "MSK", "+1234567", 1050, Pain.NO_PAIN),
    (2, "Rebrov", "Aleksandr", "Stepanovich", "TGN", "+1234567", 1060, Pain.HEAD_ACHE),
    (1, "Simachenko", "Mihail", "Leonidovich", "TGN", "+1234567", 1070, Pain.NO_PAIN),
]
patients = Patient.create_from_tup(patientsTup)

# Пациенты с головной болью
for patient in patients:
    if patient.diagnosis == Pain.HEAD_ACHE:
        print(patient)

# Пациенты с номером медкарты в интервале [1020,1060)
for patient in patients:
    if patient.card_num in range(1020, 1060):
        print(patient)
