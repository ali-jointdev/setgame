def is_a_set(cards):
    number_test = check_prop(cards[0]['number'], cards[1]['number'], cards[2]['number'])
    color_test = check_prop(cards[0]['color'], cards[1]['color'], cards[2]['color'])
    shading_test = check_prop(cards[0]['shading'], cards[1]['shading'], cards[2]['shading'])
    shape_test = check_prop(cards[0]['shape'], cards[1]['shape'], cards[2]['shape'])
    return number_test and color_test and shading_test and shape_test

def check_prop(prop1, prop2, prop3):
    all_same = prop1 == prop2 and prop2 == prop3
    all_diff = prop1 != prop2 and prop2 != prop3 and prop1 != prop3
    return all_same or all_diff
