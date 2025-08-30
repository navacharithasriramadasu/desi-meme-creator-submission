# Desi Meme Creator – Project Report

## 1. Team Information 
- **Members:**
            i) Name: Navacharitha Sriramadasu
               Mobile No: 8341590704
               registered mail-id: navacharithasriramadasu@gmail.com
            ii) Name: Regonda Shiva
               Mobile No: 7093211385
               registered mail-id: regondashiva2414@gmail.com
            iii) Name: Shaikh Amear
               Mobile No: 8106603895
               registered mail-id: 245123737115@mvsrec.edu.in
            iv) Name: Muppalla Srija Reddy
               Mobile No: 6305122949
               registered mail-id: muppallasrijareddy@gmail.com
- **Organization:** Swecha Internship Program  

---

## 2. Application Overview
The **Desi Meme Creator** is a web-based tool built using **Streamlit** that allows users to create and share memes in **multiple Indian languages**.  
- Core focus: Enable regional language meme creation to increase cultural relevance.  
- MVP Scope: Text-to-meme pipeline with language translation, font rendering, and offline-first considerations.  
- Deployment: Hosted on **Hugging Face Spaces** for free and public access.  

**App Link:** https://desi-meme-creator.streamlit.app/

---

## 3. AI Integration Details
- **Translation:** Integrated using **Deep Translator (Google Translate API)** for text localization.  
- **Meme Generation:** Uses **Pillow (PIL)** to render translated text over meme templates.  
- **AI Component:** Automated translation + language detection ensures inclusivity for non-English users.  

---

## 4. Technical Architecture & Development
- **Frontend:** Streamlit  
- **Backend:** Python (Pillow, Deep Translator, Pandas)  
- **Deployment:** Hugging Face Spaces  
- **Data Handling:**  
  - Corpus CSV file (`corpus.csv`) for saving contributions.  
  - User uploads templates and captions.  
- **Offline-first Considerations:** Lightweight architecture, minimal dependencies, works in low-bandwidth environments.  

---

## 5. User Testing & Feedback
- **Methodology:**  
  - Recruited testers from WhatsApp groups and peers.  
  - Provided them with tasks: create memes in at least 2 different languages and share feedback.    

- **Feedback:**  
  - Users appreciated the regional language support.  
  - Issues: Font rendering for certain languages, translation accuracy for idiomatic phrases.  

- **Iterations Implemented:**  
  - Added **Noto fonts** for better multi-script rendering.  
  - Improved error handling for missing translations.  
  - Optimized CSV logging of corpus data.  

---

## 6. Project Lifecycle & Roadmap  

### A. Week 1: Rapid Development Sprint  
- **Plan:** Build and deploy a functional MVP on Hugging Face Spaces.  
- **Execution:**  
  - Set up Streamlit app structure.  
  - Integrated Deep Translator for multilingual text.  
  - Implemented meme template system.  
  - Deployed successfully to Hugging Face Spaces.  

- **Key Deliverable:** Functional, deployed MVP   

---

### B. Week 2: Beta Testing & Iteration Cycle  
- **Recruitment:** 10+ testers via WhatsApp groups and peers.  
- **Tasks:** Create 3 memes each (different languages, templates).  
- **Feedback Collection:** Google Forms + direct WhatsApp messages.  

- **Insights & Iterations:**  
  - **Font Issues:** Fixed by adding **Noto font pack**.  
  - **Translation Errors:** Implemented fallback to English if translation failed.  
  - **Performance:** Reduced template image size for faster load.  

---

### C. Weeks 3–4: User Acquisition & Corpus Growth Campaign  

- **Target Audience & Channels:**  
  - College students, meme creators, and regional communities.  
  - Outreach via **WhatsApp, Instagram stories, and local cultural groups**.  

- **Growth Strategy & Messaging:**  
  - Key Message: “Create memes in your language – Desi style!”  
  - Promotional Examples:  
    - Instagram posts with sample memes.  
    - WhatsApp forwards inviting users to try the app.  

- **Execution & Results:**  
  - Promoted in 4 WhatsApp groups, 2 Instagram accounts.  
  - Collected **150+ unique memes**.  
  - Acquired **80+ unique users** in 2 weeks.  

- **Metrics:**  
  - **Corpus Units Collected:** 150+  
  - **Unique Users:** 80+  
  - **User Feedback:** Positive, especially around regional personalization.  

---

### D. Post-Internship Vision & Sustainability Plan  

- **Major Future Features:**  
  - OCR support (extract text from images).  
  - AI-driven meme caption suggestions.  
  - More templates + community uploads.  

- **Community Building:**  
  - Open contributions for templates & captions.  
  - Regular meme contests to boost engagement.  

- **Scaling Data Collection:**  
  - Crowdsourced contributions.  
  - Partnerships with local student clubs.  

- **Sustainability:**  
  - Open-source project maintained on code.swecha.org.  
  - Potential integration with WhatsApp/Telegram bots.  

---
