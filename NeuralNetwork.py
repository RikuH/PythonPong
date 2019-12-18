import pygame
from random import randint
import math

class Neuralnetwork():

    layers = []
    neurons = [[], []]
    weights = [[], [], []]
    fitness = 0

    #Constructor
    def CNeuralNetwork(self, layers):
        self.layers = len(layers)

        for x in layers:
            self.layers[x] = layers[x]

    #Copy Constructor
    def copyCNeuralNetwork(self, copy):
        self.layers = len(copy)

        for x in copy.layers:
            self.layers[x] = copy.layers[x]

    def CopyWeights(self, copyWeights):
        for x in self.weights:
            for y in self.weights[x]:
                for z in self.weights[x][y]:
                    self.weights[x][y][z] = copyWeights[x][y][z]

    def initNeurons(self):
        neuronsList = []
        for x in self.layers:
            neuronsList.insert(0, self.layers[x])

        self.neurons = neuronsList

    def InitWeights(self):
        weightsList = []
        for x in self.layers:

            layerWeightList = []
            neuronsInPreviousLayer = self.layers[x-1]

            for y in self.neurons[x]:
                neuronWeight = [neuronsInPreviousLayer]

                for z in neuronsInPreviousLayer:
                    neuronWeight[z] = randint(-0.5, 0.5)

                layerWeightList.insert(0, neuronWeight)

            weightsList.insert(0,layerWeightList)
        
        self.weights = weightsList

    def feedForward(self, inputs):
        for x in inputs:
            self.neurons[0][x] = inputs[x]

        for x in self.layers:
            for y in self.neurons[x]:
                value = 0

                for z in self.neurons[x-1]:
                    value = value + self.weights[x-1][y][z] * self.neurons[x-1][z]
                
                self.neurons[x][y] = math.tan(value)

        return self.neurons[len(self.neurons) - 1]

    def Mutate(self):
        for x in self.layers:
            for y in self.weights[x]:
                for z in self.weights[x][y]:
                    weight = weight[x][y][z]
                    randomNumber = randint(0, 100)

                    if randomNumber <= 2:
                        weight = weight * -1

                    elif randomNumber <= 4:
                        weight = randint(-0.5, 0.5)

                    elif randomNumber <= 6:
                            factor = randint(0, 1) + 1
                            weight = weight * factor
                    
                    elif randomNumber <= 8:
                        factor = randint(0, 1)
                        weight = weight * factor

                    self.weights[x][y][z] = weight

    def addFitness(self, fit):
        self.fitness = self.fitness + fit
    def setFitness(self, fit):
        self.fitness = fit
    def getFitness(self):
        return self.fitness

    def compareTo(self, other):
        if other == None:
            return 1
        if self.fitness > other.fitness:
            return 0
        elif self.fitness < other.fitness:
            return -1
        else:
            return 0