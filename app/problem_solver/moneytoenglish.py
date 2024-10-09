def money_to_english(num):
    if num < 0:
        return "negative " + money_to_english(-num)
    
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if num == 0:
        return "zero dollars"
    
    dollars = int(num)
    cents = round((num - dollars) * 100)
    
    words = []
    
    if dollars >= 1000:
        words.append(units[dollars // 1000] + " thousand")
        dollars %= 1000
    
    if dollars >= 100:
        words.append(units[dollars // 100] + " hundred")
        dollars %= 100
    
    if dollars >= 20:
        words.append(tens[dollars // 10])
        dollars %= 10
    
    if dollars >= 10:
        words.append(teens[dollars - 10])
        dollars = 0
    
    if dollars > 0:
        words.append(units[dollars])
    
    dollar_words = " ".join(words).strip() + (" dollar" if len(words) == 1 and words[0] == "one" else " dollars")
    
    if cents > 0:
        words = []
        if cents >= 20:
            words.append(tens[cents // 10])
            cents %= 10
        
        if cents >= 10:
            words.append(teens[cents - 10])
            cents = 0
        
        if cents > 0:
            words.append(units[cents])
        
        cent_words = " ".join(words).strip() + (" cent" if len(words) == 1 and words[0] == "one" else " cents")
        return f"{dollar_words} and {cent_words}"
    
    return dollar_words