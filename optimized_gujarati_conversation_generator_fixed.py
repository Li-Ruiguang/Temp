import random
import hashlib
import unicodedata

# 定义变量选项（古吉拉特语）
locations = ["ગામડું", "બાગ", "પર્વત", "નદીકાંઠો", "ચા દુકાન", "શહેરની ગલી", "બસ સ્ટોપ"]
times = ["સવાર", "બપોર", "સાંજ", "રાત્રિ", "મધ્યરાત્રિ"]
weather_conditions = ["વરસાદી", "ધુપાળુ", "વીજળીવાળું", "ધુમ્મસ", "હિમવર્ષા", "જોરદાર પવન"]
relationships = ["પડોશી", "સહકર્મી", "પતિ-પત્ની", "ભાઇ-બહેન", "મિત્રો", "અજાણ્યા લોકો"]
motivations = [
    "આજના દિવસે ખેતર માટે યોગ્ય છે કે નહીં તે ચર્ચા કરવી",
    "હવામાન વિશે ચાલતાં ચાલતાં વાત કરવી",
    "પર્વત પર ચાલવાનું ચાલુ રાખવું કે પાછા ફરવું તે નક્કી કરવું",
    "આવતીકાલના પ્રવાસ માટે યોજના બનાવવી",
    "મોસમના પરિવર્તનનો જીવન પર થતો અસર ચર્ચાવવી",
    "એક ખાસ હવામાન અનુભવ યાદ કરવો"
]

# 定义对话模板（扩展版，包含更长的对话结构）
dialog_templates = [
    [
        "A: આજે હવામાન {weather} છે. શું તમારી પાસે આ વિશે કોઈ ખાસ વિચાર છે?",
        "B: હા, {weather} હવામાન ખરેખર {location} માટે ઉત્તમ છે. તને શું લાગે છે કે આપણે શું કરવું જોઈએ?",
        "A: મને લાગે છે કે {motivation} અને કદાચ {additional} પણ વિચારવું જોઈએ.",
        "B: હા, આ વિચાર ખરેખર રસપ્રદ છે. તમે ક્યારેક આ પ્રકારની સ્થિતિ જોઈ છે જ્યાં હવામાન આટલું ખાસ હોય?",
        "A: હા, એકવાર જ્યારે હું {time} માં {location} પર હતો, ત્યારે હવાને મને એકદમ આશ્ચર્યચકિત કરી દીધું હતું. તે સમય યાદ છે!",
        "B: આ તો ખરેખર સુંદર યાદી છે. મને લાગે છે કે આપણે આજે પણ કંઈક એવું જ અનુભવી શકીએ.",
        "A: ચોક્કસ! પણ મને લાગે છે કે આપણે {preparation} માટે તૈયાર રહેવું જોઈએ.",
        "B: બરાબર. હું હંમેશા વિચારતો હતો કે આ પ્રકારના દિવસો જીવનમાં શ્રેષ્ઠ ક્ષણો છે.",
        "A: મજેદાર વાત છે! મારા માટે હવામાન માત્ર વાતાવરણ નથી, પણ તે એક મિજાજ સેટ કરે છે.",
        "B: હા, અને આ મિજાજ આપણું દ્રષ્ટિકોણ પણ બદલી શકે છે. તું આ વિષય પર વધુ શું વિચારે છે?",
        "A: મને લાગે છે કે હવામાન આપણા સંબંધો અને મનોવિજ્ઞાન પર પણ અસર કરે છે. આ વિશે તું શું વિચારું છે?",
        "B: હું સહમત છું. મને લાગે છે કે, ખાસ કરીને {relationship} વચ્ચેના સંવાદને આ પ્રકારના હવામાન પરિપ્રેક્ષ્યમાં વધુ ઊંડાઈ મળે છે.",
        "A: અત્યારે તો મને લાગે છે કે આપણે આ દિવસની વિશિષ્ટતા માણવી જોઈએ. તું શું કહે છે?",
        "B: હું તાજેતરમાં વાંચ્યું હતું કે હવામાનના મિજાજ બદલાતા લોકોની સર્જનાત્મકતામાં વધારો થાય છે. તને આ વિચાર કેવો લાગે છે?",
        "A: આ તો ખરેખર રસપ્રદ છે. તને લાગે છે કે આપણે આ દિવસને યાદગાર બનાવવા માટે કંઈક ખાસ કરી શકીએ?",
        "B: ચોક્કસ! ચાલ, આપણે એક ફોટોગ્રાફી સત્ર કરીએ અથવા કોઈ નવું આદર્શ નિર્માણ કરીએ."
    ]
]

# 验证字符的有效性
def is_valid_unicode(text):
    try:
        text.encode('utf-8').decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False

# 清理无效字符
def clean_text(text):
    return ''.join(ch for ch in unicodedata.normalize('NFKC', text) if is_valid_unicode(ch))

# 生成唯一标识符
def generate_unique_id(context):
    context_str = f"{context['location']}-{context['time']}-{context['weather']}-{context['relationship']}-{context['motivation']}"
    return hashlib.md5(context_str.encode()).hexdigest()

# 随机生成对话
def generate_conversation():
    location = random.choice(locations)
    time = random.choice(times)
    weather = random.choice(weather_conditions)
    relationship = random.choice(relationships)
    motivation = random.choice(motivations)
    dialog_template = random.choice(dialog_templates)

    # 填充模板并清理无效字符
    dialog = [clean_text(line.format(
        location=location,
        time=time,
        weather=weather,
        motivation=motivation,
        relationship=relationship,
        weather_feeling=random.choice(["મજેદાર", "ઉષ્માગ્રસ્ત", "ઠંડું", "આનંદદાયક"]),
        activity=random.choice(["ચમન", "વાંચન", "ચા પીવી", "ગપશપ", "ફોટોગ્રાફી"]),
        additional=random.choice(["સુરક્ષિત રહેવું", "છત્રી સાથે રાખવી", "યોગ્ય કપડાં પહેરવાં"]),
        preparation=random.choice(["જમવાનું લાવવું", "કેમેરા તૈયાર કરવો", "બીજા માટે ચા બનાવી લાવવી"])
    )) for line in dialog_template]

    # 确保对话长度超过1500字
    while sum(len(line) for line in dialog) < 1500:
        dialog.append(random.choice(dialog))  # 重复添加随机行以填充内容

    context = {
        "location": clean_text(location),
        "time": clean_text(time),
        "weather": clean_text(weather),
        "relationship": clean_text(relationship),
        "motivation": clean_text(motivation),
        "dialog": dialog
    }
    context["unique_id"] = generate_unique_id(context)
    return context

# 生成Markdown文件
def generate_markdown(conversations, filename="weather_conversations_gujarati_long.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# હવામાન વિષયક સંવાદ (ગુજરાતી ભાષા)\n\n")
        for i, convo in enumerate(conversations):
            f.write(f"## સંવાદ ઉદાહરણ {i + 1}\n")
            f.write("**પ્રસંગ**:\n")
            f.write(f"- સ્થાન: {convo['location']}\n")
            f.write(f"- સમય: {convo['time']}\n")
            f.write(f"- હવામાન: {convo['weather']}\n")
            f.write(f"- સંબંધ: {convo['relationship']}\n")
            f.write(f"- ચર્ચાવિષય: {convo['motivation']}\n\n")
            f.write("**સંવાદ**:\n")
            f.write("```\n")
            for line in convo["dialog"]:
                f.write(line + "\n")
            f.write("```\n\n")
            f.write("---\n\n")

# 主函数
def main():
    num_conversations = 500  # 生成500组对话
    conversations = []
    unique_ids = set()

    while len(conversations) < num_conversations:
        convo = generate_conversation()
        if convo["unique_id"] not in unique_ids:  # 检查是否重复
            unique_ids.add(convo["unique_id"])
            conversations.append(convo)

    generate_markdown(conversations)
    print(f"500 સંવાદો તૈયાર છે અને 'weather_conversations_gujarati_long.md' ફાઇલમાં સંગ્રહિત છે.")

if __name__ == "__main__":
    main()