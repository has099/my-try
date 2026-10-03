import os

print("=" * 50)
print("🤖 أهلاً بك في مصنع السكربتات والأكواد الآلي")
print("=" * 50)

print("\nاختر نوع السكربت الذي تريد صنعه:")
print("1️⃣ سكربت تشفير ملفات (Python Fernet)")
print("2️⃣ سكربت فحص شبكة سريع (Ping Scanner)")
print("3️⃣ سكربت دفتر ملاحظات نصي بسيط")

choice = input("\nاكتب رقم الخيار (1، 2، أو 3): ").strip()

# قاعدة بيانات للأكواد الجاهزة التي يمكن للتطبيق تركيبها وتصديرها
scripts_db = {
    "1": {
        "name": "encryption_tool.py",
        "code": """# سكربت تشفير تلقائي
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
print("تم إنشاء مفتاح التشفير بنجاح!")
message = "رسالة سرية للغاية"
encrypted = fernet.encrypt(message.encode())
print("النص المشفر:", encrypted)
"""
    },
    "2": {
        "name": "network_scanner.py",
        "code": """# سكربت فحص الشبكة
import os
print("جاري فحص الاتصال بالشبكة المحلية...")
response = os.system("ping -c 1 8.8.8.8")
if response == 0:
    print("🟢 متصل بالإنترنت بنجاح!")
else:
    print("🔴 لا يوجد اتصال!")
"""
    },
    "3": {
        "name": "simple_diary.py",
        "code": """# سكربت دفتر ملاحظات
note = input("اكتب ملاحظتك لحفظها: ")
with open("note.txt", "w", encoding="utf-8") as f:
    f.write(note)
print("✅ تم حفظ الملاحظة في ملف note.txt بنجاح!")
"""
    }
}

if choice in scripts_db:
    selected_script = scripts_db[choice]
    filename = selected_script["name"]
    file_code = selected_script["code"]
    
    # حفظ الكود تلقائياً في ملف بايثون حقيقي
    with open(filename, "w", encoding="utf-8") as f:
        f.write(file_code)
        
    print(f"\n✨ مبروك! قام التطبيق بتأليف وكتابة السكربت بنجاح.")
    print(f"📦 تم حفظ السكربت في ملف باسم: {filename}")
    print("\n--- محتوى السكربت الذي تم توليده: ---")
    print(file_code)
    print("-" * 40)
    
else:
    print("\n❌ خيار غير صحيح، يرجى اختيار رقم من القائمة.")
