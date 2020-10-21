from src.main import NeuralNetwork


def test_get_attr():
    neural_network = NeuralNetwork(1, 2, 3, 4)
    attribute = neural_network.get_attr()
    assert attribute == 1
