import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np. array([[0,1,1,1,0],
                             [1,0,0,0,1],
                             [0,1,0,0,1],
                             [1,0,1,0,0],
                             [0,0,0,1,0],
                             [1,1,1,0,0],
                             [0,1,0,1,1],
                             [1,0,1,0,1]])

training_outputs = np.array([[0,1,0,1,0,1,0,1]]).T
np.random.seed(1)
synaptic_weights = 2 * np.random.random((5,1))-1

for i in range(30000):
    input_layer = training_inputs
    outputs = sigmoid( np.dot(input_layer, synaptic_weights) )
    err = training_outputs - outputs
    adjstmnts = np.dot(input_layer.T, err*(outputs*(1-outputs)))
    synaptic_weights+=adjstmnts

#TEST

new_inputs = np.array([0,1,1,0,1])
output = sigmoid(np.dot(new_inputs, synaptic_weights))

print("Суть логоволомки в том что нам дается список из пяти элементов, каждый из которого может быть равен 1 или 0\n"
      "так например если у нас строка 1, 0, 1, 0, 1, то ответ будет 1, если же 0, 1, 1, 1, 1, то ответ уже будет 0\n"
      "то есть ответ зависит от первого элемента, но ИИ не знает об этом, поэтому он обучается 30 000 раз и только после \n"
      "этого пытается решить задачку которую мы задаем, на которую ранее не было ответа в данных на которых он обучался.\n"
      "Вот массив с входными данными на которых он обучался:\n", training_inputs, "\n а вот и соответствующие ответы\n",training_outputs
      ,"Теперь на вход мы даем массив из пяти элементов и получаем от ИИ вероятность того что ответ к данному нами массиву\n "
       "будет равна единице")

print(new_inputs)
print("Ответ на задачку:")
print(output)