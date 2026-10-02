#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from .frenchdeck import FrenchDeck, Card
except ImportError:  # Support direct execution as a script.
    from frenchdeck import FrenchDeck, Card
import random

def main():
    # 创建一个FrenchDeck实例
    deck = FrenchDeck()
    
    # 测试__len__方法
    print("Deck length: {}".format(len(deck)))
    
    # 测试__getitem__方法 - 通过索引访问
    print("First card: {}".format(deck[0]))
    print("Last card: {}".format(deck[-1]))
    print("Random card: {}".format(deck[10]))
    
    # 测试随机抽取牌
    print("Random card (using random.choice): {}".format(random.choice(deck)))
    
    # 测试切片
    print("First three cards:")
    for card in deck[:3]:
        print("  {}".format(card))
    
    # 测试迭代
    print("\nSome cards:")
    for card in deck[:5]:
        print("  {}".format(card))
    
    # 测试in操作符
    print("\nChecking if Card('Q', 'hearts') is in deck:")
    print(Card('Q', 'hearts') in deck)
    print("Checking if Card('7', 'beasts') is in deck:")
    print(Card('7', 'beasts') in deck)


if __name__ == '__main__':
    main()
