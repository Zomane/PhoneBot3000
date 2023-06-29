import numpy as np
import re

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def preprocess_text(text):
    # Извлечение чисел из текста
    numbers = re.findall(r'\d+', text)
    return [int(num) for num in numbers]

# Ваши текстовые данные для обучения
input_data = [
    "Было 2 яблока, одно съели",
    "В корзине было 3 груши, к ним положили еще 1",
    "Было 3 банана, два съели",
    "В корзине было 3 апельсины, к ним положили еще 2",
    "Было 5 мандарина, три съели",
    "В корзине было 3 киви, к ним положили еще 3",
    "Было 4 арбуза, один съели",
    "В корзине было 3 дыни, к ним положили еще 4",
    "Было 9 вишни, семь съели",
    "В корзине было 3 клубники, к ним положили еще 1",
    "Было 7 малины, две съели",
    "В корзине было 3 смородины, к ним положили еще 2",
    "Было 3 яблока, 3 съели",
    "В корзине было 3 груши, к ним положили еще 4",
    "Было 4 яблока, одно съели",
    "В корзине было 3 груши, к ним положили еще 5",
    "Было 3 яблока, одно съели",
    "В корзине было 5 груш, к ним положили еще 1"
]

# Преобразование текстовых данных в числовые входные данные
training_inputs = [preprocess_text(text) for text in input_data]

# Определение максимальной длины входных данных
max_input_length = max(len(inputs) for inputs in training_inputs)

# Заполнение недостающих элементов нулями
training_inputs = [inputs + [0] * (max_input_length - len(inputs)) for inputs in training_inputs]

# Преобразование входных данных в массив numpy
training_inputs = np.array(training_inputs)

# Ожидаемые выходы
training_outputs = np.array([[1], [4], [1], [5], [2], [6], [3], [7], [2], [4], [5], [5], [0], [7], [3], [8], [2], [6]])  # Замените ... на ожидаемые выходы

np.random.seed(2)
synaptic_weights = 2 * np.random.random((max_input_length, 1)) - 1

for i in range(50000):
    input_layer = training_inputs
    outputs = tanh(np.dot(input_layer, synaptic_weights))
    err = training_outputs - outputs
    adjstmnts = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
    synaptic_weights += adjstmnts

# TEST

new_text = "В корзине было 1 груш, к ним положили еще 7"
new_inputs = preprocess_text(new_text)
new_inputs = new_inputs + [0] * (max_input_length - len(new_inputs))
new_inputs = np.array([new_inputs])  # Добавьте дополнительные квадратные скобки для создания двумерного массива
output = tanh(np.dot(new_inputs, synaptic_weights))

print("Ответ на задачку:")
print(output)
