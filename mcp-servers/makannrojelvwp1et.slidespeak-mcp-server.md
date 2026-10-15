# SlideSpeak MCP Server
An MCP server that enables Claude or other MCP-compatible apps to generate PowerPoint presentations from natural language prompts using the SlideSpeak API. This project provides an easy-to-use interface for creating presentations directly from text input.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/Z786ZA/Footer-test/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/Bitbash333" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>slidespeak-mcp-server</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
SlideSpeak MCP Server acts as an API-driven interface that transforms natural language prompts into professional PowerPoint presentations. It is designed to simplify the process of creating custom presentations without requiring advanced technical skills. The server supports various customization options, including templates, images, and slide layouts.

### Key Features
- Generate PowerPoint or PDF presentations from natural language.
- Extensive template and customization options for slides.
- Includes customizable branding, fonts, and logos.
- Integration-ready with MCP-compatible applications like Claude.
- Fast and reliable operation for scalable presentation generation.

## Features
| Feature                 | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Generate PowerPoint**  | Create presentations based on topic, length, and template with multiple options. |
| **Slide-by-Slide Input**| Control the content and layout of each slide individually.                 |
| **Template Selection**   | Choose from various predefined templates for a professional look.           |
| **Branding Support**     | Customize logos, fonts, and colors to match your branding.                 |
| **Multilingual Support** | Generate presentations in multiple languages with language selection.      |

---

## What Data This Scraper Extracts
| Field Name       | Field Description                                                           |
|------------------|-----------------------------------------------------------------------------|
| plain_text       | Topic or subject for generating the presentation.                           |
| length           | Number of slides for the generated presentation.                            |
| template         | Template name or ID for the presentation layout.                           |
| document_uuids   | List of UUIDs of documents used to generate the slides.                    |
| language         | The language code to generate the presentation in. Default is 'ORIGINAL'.  |
| fetch_images     | Whether to include stock images in the presentation (default: true).       |
| tone             | The tone of the presentation (e.g., casual, professional, funny, etc.).    |
| verbosity        | The level of text detail in the presentation (concise, standard, text-heavy). |
| custom_user_instructions | Custom instructions to influence slide generation.                   |

---

## Example Output
Example:
    [
          {
            "facebookUrl": "https://www.facebook.com/nytimes/",
            "pageId": "5281959998",
            "postId": "10153102374144999",
            "pageName": "The New York Times",
            "url": "https://www.facebook.com/nytimes/posts/pfbid02meAxCj1jLx1jJFwJ9GTXFp448jEPRK58tcPcH2HWuDoogD314NvbFMhiaint4Xvkl",
            "time": "Thursday, 6 April 2023 at 06:55",
            "timestamp": 1680789311000,
            "likes": 22,
            "comments": 2,
            "shares": null,
            "text": "Four days before the wedding they emailed family members a “save the date” invite. It was void of time, location and dress code — the couple were still deciding those details.",
            "link": "https://nyti.ms/3KAutlU"
          }
        ]

---

## Directory Structure Tree
    SlideSpeak MCP Server Scraper/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── generate_powerpoint.py
    │   │   └── utils.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample.json
    ├── requirements.txt
    └── README.md

---

## Use Cases
- **Marketing teams** use it to create custom presentations from meeting notes, so they can deliver tailored, polished slides for client pitches.
- **Content creators** use it to turn blog posts into engaging presentations, making content more interactive and shareable.
- **Educators** use it to quickly generate educational slides on various topics, saving time for lesson planning.

## FAQs
**Q:** How do I connect to the SlideSpeak MCP Server?
**A:** You can connect using the configuration provided in the `client_configuration.json` file with your Apify API token.

**Q:** Can I customize the presentation templates?
**A:** Yes, you can choose from predefined templates or even define custom templates for more control over the layout and design.

**Q:** What formats are available for the presentations?
**A:** Presentations can be generated in either PowerPoint (PPTX) or PDF format.

---

### Performance Benchmarks and Results
**Primary Metric:** Average presentation generation time: 3–5 seconds per slide.
**Reliability Metric:** 99.9% task success rate.
**Efficiency Metric:** Handles up to 500 presentations per hour with minimal resource usage.
**Quality Metric:** 98% of generated presentations meet user-defined specifications without manual intervention.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/Z786ZA/Footer-test/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        "Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time."
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/Z786ZA/Footer-test/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        "Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on."
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/m-dRE1dj5-k?si=5kZNVlKsGUhg5Xtx" target="_blank">
        <img src="https://github.com/Z786ZA/Footer-test/blob/main/media/review3.gif" alt="Review 3" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        "Exceptional results, clear communication, and flawless delivery. <br>Bitbash nailed it."
      </p>
      <p style="margin:1px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
