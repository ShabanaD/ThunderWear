import math
import json
import operator
import os
import random

class Outfit:

    def __init__(self, weatherInfo):
        
        self.outfit = {  "top":"",
                        "bottoms":"",
                        "jacket":"",
                        "dress":""
                        }

        # Returns temperature, a key word - clear, rain, hail, snow?
        self.weather = weatherInfo
        self.jackets = []
        tops = self.getTop()
        bottoms = self.getBottoms()
        dresses = self.getDress()
        self.makeOutfit(tops, bottoms, self.jackets)

    def getTop(self):
        tops = ["button", "blouse", "shirt", "top"] 

        t = open("tops.txt", "r")
        temp = t.readline().split("?")
        matches = []
        alltops = []
        # Split them all into 2d array
        for top in temp:
            alltops.append(top.split("!"))

        alltops = alltops[:-1]

        if (self.weather["cond"]=="clear"):
            # If hot, output anything with shirt and top
            if (self.weather["temp"] >= 25):
                for top in alltops:
                    if any(s in top[1] for s in ["shirt", "top"]):
                        matches.append(top[0])
            # Cold
            elif (self.weather["temp"] <= 5):
                for top in alltops:
                    if any(s in top[1] for s in ["sweatshirt","button"]):
                        matches.append(top[0])
                self.getJacket()        
            # Warm
            elif (self.weather["temp"] >= 20 and self.weather["temp"] < 25):
                for top in alltops:
                    if any(s in top[1] for s in tops):
                        matches.append(top[0])
            # Cool    
            elif (self.weather["temp"] < 20 and self.weather["temp"] > 5):
                for top in alltops:
                    if any(s in top[1] for s in tops):
                        matches.append(top[0])
                self.getJacket()

        elif (self.weather["cond"]=="rain") or (self.weather["cond"]=="snow"):
            self.getJacket()
            for top in alltops:
                if any(s in top[1] for s in tops):
                    matches.append(top[0])
                      
        elif (self.weather["cond"]=="snow"):
            for top in alltops:
                if any(s in top[1] for s in tops):
                    matches.append(top[0])
            self.getJacket()

        return matches

    def getBottoms(self):
        bottoms = ["pants", "skirt", "trousers", "denim", "jeans", "shorts", "slacks"]
        b = open("bottoms.txt", "r")
        temp = b.readline().split("?")
        matches = []
        allbots = []
        # Split them all into 2d array
        for bot in temp:
            allbots.append(bot.split("!"))

        allbots = allbots[:-1]

        if (self.weather["cond"]=="clear"):
            # If hot, output anything with shirt and top
            if (self.weather["temp"] >= 25):
                for bot in allbots:
                    if any(s in bot[1] for s in ["shorts", "skirt"]):
                        matches.append(bot[0])
            # Cold
            elif (self.weather["temp"] <= 5):
                for bot in allbots:
                    if any(s in bot[1] for s in ["pants","jeans", "trousers", "denim", "slacks"]):
                        matches.append(bot[0])       
            # Warm
            elif (self.weather["temp"] >= 20 and self.weather["temp"] < 25):
                for bot in allbots:
                    if any(s in bot[1] for s in bottoms):
                        matches.append(bot[0])
            # Cool    
            elif (self.weather["temp"] < 20 and self.weather["temp"] > 5):
                for bot in allbots:
                    if any(s in bot[1] for s in bottoms):
                        matches.append(bot[0])

        elif (self.weather["cond"]=="rain") or (self.weather["cond"]=="snow"):
            for bot in allbots:
                 if any(s in bot[1] for s in ["pants","jeans", "trousers", "denim", "slacks"]):
                    matches.append(bot[0])         
        elif (self.weather["cond"]=="snow"):
            for bot in allbots:
                if any(s in bot[1] for s in ["pants","jeans", "trousers", "denim", "slacks"]):
                    matches.append(bot[0])
        return matches

    def getJacket(self):
        jackets = ["coat", "snowsuit", "jacket", "windbreaker", "windcheater", "sweater", "cardigan", "vest"]
        matches = []
        j = open("jackets.txt", "r")
        temp = j.readline().split("?")
        alljacs = []
        for jac in temp:
            alljacs.append(jac.split("!"))

        alljacs = alljacs[:-1]
        if (self.weather["cond"]=="clear"):
            # If hot, output anything with shirt and top
            if (self.weather["temp"] >= 25):
                for jac in alljacs:
                    if any(s in jac[1] for s in ["cardigan"]):
                        matches.append(jac[0])
            # Cold
            elif (self.weather["temp"] <= 5):
                for jac in alljacs:
                    if any(s in jac[1] for s in ["coat", "snowsuit", "jacket","sweater"]):
                        matches.append(jac[0])       
            # Warm
            elif (self.weather["temp"] >= 20 and self.weather["temp"] < 25):
                for jac in alljacs:
                    if any(s in jac[1] for s in jackets):
                        matches.append(jac[0])
            # Cool    
            elif (self.weather["temp"] < 20 and self.weather["temp"] > 5):
                for jac in alljacs:
                    if any(s in jac[1] for s in jackets):
                        matches.append(jac[0])

        elif (self.weather["cond"]=="rain") or (self.weather["cond"]=="snow"):
            for jac in alljacs:
                if any(s in jac[1] for s in ["coat", "snowsuit", "jacket","sweater"]):
                    matches.append(jac[0])
        elif (self.weather["cond"]=="snow"):
            for jac in alljacs:
                if any(s in jac[1] for s in ["coat", "jacket","sweater"]):
                    matches.append(jac[0])
        self.jackets = matches

    def getDress(self):
        matches = []
        return matches

    def makeOutfit(self, t, b, j):
        if t:
            self.outfit["top"] = random.choice(t)
        if b:
            self.outfit["bottoms"] = random.choice(b)
        if j:
            self.outfit["jacket"] = random.choice(j)
    
        
