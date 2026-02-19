# ASK DOC AI   
**اسأل عقدك أي سؤال.. بالعامية أو بالفصحى**

تطبيق ذكي يعتمد على RAG (Retrieval-Augmented Generation) يسمح لك برفع عقد ذكي أو أي وثيقة قانونية (PDF أو DOCX)، ثم تسأل عن أي بند أو شرط أو التزام بلغة طبيعية، والإجابات تأتي مدعومة بنصوص العقد الفعلية + يتذكر سياق المحادثة السابقة.

### لماذا هذا المشروع مفيد؟
- يشرح العقود المعقدة بلغة بسيطة وواضحة  
- يجاوب على أسئلة دقيقة (مثل: مين مسؤول عن إيه؟ فيه غرامات؟ شرط تعسفي؟ ...)  
- يحتفظ بذاكرة المحادثة داخل الجلسة الواحدة  
- سرعة استجابة عالية جدًا بفضل Groq + Llama 3.1  
- واجهة سهلة الاستخدام + API قوي جاهز للتطوير

---

### المميزات الرئيسية

- رفع ملفات العقود (PDF / DOCX)  
- تقسيم ذكي للنصوص + embeddings عالية الجودة  
- قاعدة بيانات فيكتور محلية (Chroma)  
- سلسلة RAG كاملة مع دعم الذاكرة  
- نموذج لغة سريع وقوي: Llama-3.1-8B عبر Groq  
- واجهة دردشة مريحة مبنية على Gradio  
- تقييم أولي لجودة الإجابات (مستوحى من G-Eval)  
- API مكشوف وجاهز للتكامل (FastAPI + LangServe)

---

### التقنيات المستخدمة

- **Backend & API** → FastAPI + LangChain (LCEL) + LangServe  
- **Embeddings** → sentence-transformers/all-MiniLM-L6-v2  
- **Vector Store** → Chroma  
- **LLM** → Groq (Llama-3.1-8b-instant)  
- **Frontend** → Gradio  
- **Python** → 3.11+

---

### ابدأ في ٤–٦ دقائق

1. استنسخ المشروع
   ```bash
   git clone https://github.com/Omar113650/ASKDOS-.git
   cd ASKDOS-

أنشئ بيئة افتراضية وفعّلهاBashpython -m venv venv
# Windows:
venv\Scripts\activate
# Linux / macOS:
# source venv/bin/activate
ثبت المتطلباتBashpip install -r requirements.txt
أضف مفتاح Groq
أنشئ ملف .env في الجذر وحط فيه:textGROQ_API_KEY=gsk_...
شغّل الـ BackendBashuvicorn backend.main:app --reload --port 8000
شغّل الواجهة (في نافذة terminal جديدة)Bashpython frontend/app.py

→ افتح المتصفح على: http://127.0.0.1:7860

أمثلة على الأسئلة اللي بتشتغل ممتاز

فين شرط الإنهاء في العقد؟
مين المسؤول عن التعويضات في حالة التأخير؟
هل فيه بند قوة قاهرة؟
لخص الالتزامات المالية والغرامات
هل يوجد حد أقصى للمسؤولية؟
ما الفرق بين البند 5 والبند 12؟


هيكل المشروع (الأساسي)
textASKDOS-/
├── backend/
│   ├── ingestion.py          # رفع وتجهيز الوثائق + بناء الفيكتور
│   ├── rag_chain.py          # سلسلة RAG + الذاكرة
│   ├── main.py               # الـ API والروتات
│   └── evaluation/           # تقييم الإجابات
│       ├── dataset.json
│       ├── evaluator.py
│       ├── geval_judge.py
│       └── metrics.py
├── frontend/
│   └── app.py                # واجهة Gradio
├── data/                     # (مُتجاهل) ملفات العقود المرفوعة
├── chroma_db/                # (مُتجاهل) قاعدة الفيكتور
├── assets/                   # فيديوهات أو صور توضيحية
├── .env.example
├── requirements.txt
└── README.md

الخطط المستقبلية (To-Do List)

حفظ الجلسات بشكل دائم (Redis / SQLite)
دعم عدة مستخدمين + تسجيل دخول بسيط
إجابات streaming (تظهر تدريجيًا)
تحسين الاسترجاع (reranker – query rewriting – HyDE)
دعم ملفات مسحوبة (OCR للـ scanned PDFs)
حاويات Docker + docker-compose
لوحة مقارنة وتقييم أفضل للإجابات
دعم نماذج محلية (Ollama) كبديل اختياري