import pica
import time


def sum_and_mult_test():
    g = pica.Graph()
    v1 = pica.VariableNode(2)
    v2 = pica.VariableNode(5)
    v3 = pica.VariableNode(20)
    v4 = pica.MultNode(v2, v3)
    v5 = pica.SumNode(v1, v4)
    g.node(v1)
    g.node(v2)
    g.node(v3)
    g.connect(v2, v4)
    g.connect(v3, v4)
    g.connect(v1, v5)
    g.connect(v4, v5)
    result = g.forward()
    g.backward()
    assert (
        result == 102 and v1.gradient == 1 and v2.gradient == 20 and v3.gradient == 5
    ), "Sum and Mult Test Failed"
    print("Success Sum and Mult Test")


def sub_and_div_test():
    g = pica.Graph()
    v1 = pica.VariableNode(5)
    v2 = pica.VariableNode(6)
    v3 = pica.VariableNode(7)
    v4 = pica.ValueNode(9)
    v5 = pica.SubNode(v1, v2)
    v6 = pica.MultNode(v4, v3)
    v7 = pica.DivNode(v5, v6)
    g.node(v1)
    g.node(v2)
    g.node(v3)
    g.node(v4)
    g.connect(v1, v5)
    g.connect(v2, v5)
    g.connect(v3, v6)
    g.connect(v4, v6)
    g.connect(v5, v7)
    g.connect(v6, v7)
    result = g.forward()
    g.backward()
    assert (
        result == -0.015873015873015872
        and v1.gradient == 0.015873015873015872
        and v2.gradient == -0.015873015873015872
        and v3.gradient == 0.0022675736961451248
    ), "Sub and Div Test Failed"
    print("Success Sub and Div Test")


def trig_test_1():
    g = pica.Graph()
    v1 = pica.VariableNode(3)
    v2 = pica.VariableNode(17)
    v3 = pica.VariableNode(22)
    v4 = pica.SinNode(v1)
    v5 = pica.CosNode(v2)
    v6 = pica.TanNode(v3)
    v7 = pica.MultNode(v5, v6)
    v8 = pica.SubNode(v4, v7)
    g.node(v1)
    g.node(v2)
    g.node(v3)
    g.connect(v1, v4)
    g.connect(v2, v5)
    g.connect(v3, v6)
    g.connect(v5, v7)
    g.connect(v6, v7)
    g.connect(v5, v8)
    g.connect(v7, v8)
    result = g.forward()
    g.backward()

    assert (
        result == -0.334036245057012
        and v1.gradient == 0.9986295347545738
        and v2.gradient == 0.11812583640011823
        and v3.gradient == -1.1124092582218779
    ), "Trig Test 1 Failed"
    print("Success Trig Test 1")


def trig_test_2():
    g = pica.Graph()
    v1 = pica.VariableNode(55)
    v2 = pica.VariableNode(60)
    v3 = pica.CscNode(v1)
    v4 = pica.MultNode(v1, v2)
    v5 = pica.DivNode(v3, v4)
    g.node(v1)
    g.node(v2)
    g.connect(v1, v3)
    g.connect(v1, v4)
    g.connect(v2, v4)
    g.connect(v3, v5)
    g.connect(v4, v5)
    result = g.forward()
    g.backward()
    assert (
        result == 0.0003699316935640776
        and v1.gradient == -0.0002657549912483257
        and v2.gradient == -6.16552822606796e-06
    ), "Trig Test 2 Failed"
    print("Success Trig Test 2")


def logs_test():
    g = pica.Graph()
    v1 = pica.VariableNode(3)
    v2 = pica.VariableNode(9)
    v3 = pica.LnNode(v1)
    v4 = pica.LogNode(v2)
    v5 = pica.MultNode(v3, v4)
    v6 = pica.TanNode(v1)
    v7 = pica.CotNode(v2)
    v8 = pica.MultNode(v6, v7)
    v9 = pica.DivNode(v5, v8)
    g.node(v1)
    g.node(v2)
    g.connect(v1, v3)
    g.connect(v2, v4)
    g.connect(v3, v5)
    g.connect(v4, v5)
    g.connect(v1, v6)
    g.connect(v2, v7)
    g.connect(v6, v8)
    g.connect(v7, v8)
    g.connect(v5, v9)
    g.connect(v8, v9)
    result = g.forward()
    g.backward()
    assert (
        result == 3.1682538333896275
        and v1.gradient == -59.658635964251935
        and v2.gradient == 20.66558448959415
    ), "Logarithms Test Failed"
    print("Success Logarithms Test")


def power_test():
    g = pica.Graph()
    v1 = pica.ValueNode(2)
    v2 = pica.ValueNode(15)
    v3 = pica.VariableNode(3)
    v4 = pica.VariableNode(5)
    v5 = pica.SinNode(v3)
    v6 = pica.PowerNode(v5, v1)
    v7 = pica.PowerNode(v2, v4)
    v8 = pica.SumNode(v6, v7)
    g.node(v1)
    g.node(v2)
    g.node(v3)
    g.node(v4)
    g.connect(v3, v5)
    g.connect(v1, v6)
    g.connect(v5, v6)
    g.connect(v2, v7)
    g.connect(v4, v7)
    g.connect(v6, v8)
    g.connect(v7, v8)
    result = g.forward()
    g.backward()
    assert (
        result == 759375.0027390523
        and v3.gradient == 0.10452846326765347
        and v4.gradient == 2056425.6214619908
    ), "Power Test Failed"
    print("Success Power Test")


def hyp_test():
    g = pica.Graph()
    v1 = pica.VariableNode(0.3)
    v2 = pica.VariableNode(0.5)
    v3 = pica.VariableNode(0.75)
    v4 = pica.SinhNode(v1)
    v5 = pica.CoshNode(v2)
    v6 = pica.TanhNode(v3)
    v7 = pica.MultNode(v5, v6)
    v8 = pica.SumNode(v4, v7)

    g.node(v1)
    g.node(v2)
    g.node(v3)
    g.connect(v1, v4)
    g.connect(v2, v5)
    g.connect(v3, v6)
    g.connect(v5, v7)
    g.connect(v6, v7)
    g.connect(v4, v8)
    g.connect(v7, v8)

    result = g.forward()
    g.backward()
    assert (
        result == 1.020730743932679
        and v1.gradient == 1.0453385141288605
        and v2.gradient == 0.3309731373782871
        and v3.gradient == 0.672725647891665
    ), "Hyperbolic Test Failed"
    print("Success Hyperbolic Test")


sum_and_mult_test()
sub_and_div_test()
trig_test_1()
trig_test_2()
logs_test()
power_test()
hyp_test()
