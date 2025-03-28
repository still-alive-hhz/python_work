# This program allows users to query amino acids based on RNA codons or anticodons.

# 完整的密码子到氨基酸的对照字典
codon_table = {
    "UUU": "苯丙氨酸", "UUC": "苯丙氨酸",
    "UUA": "亮氨酸", "UUG": "亮氨酸",
    "CUU": "亮氨酸", "CUC": "亮氨酸",
    "CUA": "亮氨酸", "CUG": "亮氨酸",
    "AUU": "异亮氨酸", "AUC": "异亮氨酸",
    "AUA": "异亮氨酸", "AUG": "甲硫氨酸（起始密码子）",
    "GUU": "缬氨酸", "GUC": "缬氨酸",
    "GUA": "缬氨酸", "GUG": "缬氨酸",
    "UCU": "丝氨酸", "UCC": "丝氨酸",
    "UCA": "丝氨酸", "UCG": "丝氨酸",
    "CCU": "脯氨酸", "CCC": "脯氨酸",
    "CCA": "脯氨酸", "CCG": "脯氨酸",
    "ACU": "苏氨酸", "ACC": "苏氨酸",
    "ACA": "苏氨酸", "ACG": "苏氨酸",
    "GCU": "丙氨酸", "GCC": "丙氨酸",
    "GCA": "丙氨酸", "GCG": "丙氨酸",
    "UAU": "酪氨酸", "UAC": "酪氨酸",
    "UAA": "终止密码子", "UAG": "终止密码子",
    "CAU": "组氨酸", "CAC": "组氨酸",
    "CAA": "谷氨酰胺", "CAG": "谷氨酰胺",
    "AAU": "天冬酰胺", "AAC": "天冬酰胺",
    "AAA": "赖氨酸", "AAG": "赖氨酸",
    "GAU": "天冬氨酸", "GAC": "天冬氨酸",
    "GAA": "谷氨酸", "GAG": "谷氨酸",
    "UGU": "半胱氨酸", "UGC": "半胱氨酸",
    "UGA": "终止密码子", "UGG": "色氨酸",
    "CGU": "精氨酸", "CGC": "精氨酸",
    "CGA": "精氨酸", "CGG": "精氨酸",
    "AGU": "丝氨酸", "AGC": "丝氨酸",
    "AGA": "精氨酸", "AGG": "精氨酸",
    "GGU": "甘氨酸", "GGC": "甘氨酸",
    "GGA": "甘氨酸", "GGG": "甘氨酸"
}

# 碱基互补配对规则
complementary_base = {
    "A": "U",
    "U": "A",
    "C": "G",
    "G": "C"
}

def display_intro():
    """显示程序功能介绍"""
    print("欢迎使用密码子和反密码子查询氨基酸的工具！")
    print("功能介绍：")
    print("1. 您可以输入密码子（三个碱基）来查询对应的氨基酸。")
    print("2. 您也可以输入反密码子，程序会自动将其转换为密码子并查询对应的氨基酸。")
    print("3. 如果输入有误，程序会提示您重新输入。")
    print("4. 查询完成后，您可以选择继续查询或退出程序。")
    print("---------------------------------------------------")

def translate_anticodon_to_codon(anticodon):
    """将反密码子翻译为密码子"""
    try:
        return "".join(complementary_base[base] for base in anticodon)
    except KeyError:
        return None

def query_amino_acid():
    while True:
        print("请选择输入类型：1. 密码子  2. 反密码子")
        choice = input("请输入选项（1 或 2）：").strip()

        if choice == "1":
            codon = input("请输入密码子（三个碱基）：").strip().upper()
            amino_acid = codon_table.get(codon)
            if amino_acid:
                print(f"密码子 {codon} 对应的氨基酸是：{amino_acid}")
            else:
                print(f"你输入的密码子 {codon} 可能有误，请重新输入。")
        
        elif choice == "2":
            anticodon = input("请输入反密码子（三个碱基）：").strip().upper()
            codon = translate_anticodon_to_codon(anticodon)
            if codon:
                print(f"你输入的反密码子对应的密码子为：{codon}")
                amino_acid = codon_table.get(codon)
                if amino_acid:
                    print(f"密码子 {codon} 对应的氨基酸是：{amino_acid}")
                else:
                    print(f"你输入的反密码子转化的密码子 {codon} 可能有误，请重新输入。")
            else:
                print(f"你输入的反密码子 {anticodon} 可能有误，请重新输入。")
        
        else:
            print("无效的选项，请重新输入。")
            continue

        # 询问是否继续
        again = input("是否继续查询？（y/n）：").strip().lower()
        if again != "y":
            print("程序结束，再见！")
            break

# 启动程序
if __name__ == "__main__":
    display_intro()
    query_amino_acid()

# Designed by Still_Alive with Github Copilot
# 2025.03.28