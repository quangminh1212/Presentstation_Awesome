# PitchForge AI

Turn Technical Docs into Investor-Ready Pitches. 

PitchForge AI is an AI Product Consultant that reads your technical documentation (like READMEs), detects business gaps, and generates beautiful, logic-driven presentations. Built for founders, driven by logic, and powered by the Algorand blockchain for frictionless x402 microtransactions.

## 🚀 Features

- **README Parsing:** Drop your GitHub repository or Markdown documentation. The AI instantly extracts your architecture and features.
- **Gap Detection:** Our AI Consultant analyzes your documentation, identifying missing business logic to perfect your pitch and investor readiness.
- **AI-Generated Presentations:** Generates high-quality pitch decks utilizing Google Gemini, automatically structured with beautiful slide layouts.
- **Visuals Included:** Uses Pollinations AI to automatically generate relevant and stunning visuals for your pitch deck slides.
- **x402 Microtransactions Export:** Download your generated presentations instantly via frictionless Algorand microtransactions.
- **PPTX Export:** Export the generated presentation directly to a `.pptx` PowerPoint file ready for use.

## 🛠 Tech Stack

- **Framework:** [Next.js](https://nextjs.org/) (App Router, React 19)
- **Styling:** [Tailwind CSS](https://tailwindcss.com/) & [shadcn/ui](https://ui.shadcn.com/)
- **AI Integration:** [Vercel AI SDK](https://sdk.vercel.ai/) & Google Gemini (gemini-3.5-flash-lite)
- **Blockchain Integration:** Algorand Wallet Ecosystem (`@txnlab/use-wallet-react`, Pera Wallet, Defly, Lute, WalletConnect)
- **State Management:** [Zustand](https://zustand-demo.pmnd.rs/)
- **PPT Generation:** [pptxgenjs](https://gitbrent.github.io/PptxGenJS/)

## 📂 Project Structure

```
pitchforge-ai/
├── src/
│   ├── app/                 # Next.js App Router pages and layouts
│   │   ├── api/             # API Routes (AI endpoints, GitHub parsing, etc.)
│   │   ├── app/             # Application dashboard routes (upload, consult, build, presentation)
│   │   └── globals.css      # Global styles
│   ├── components/          # Reusable React components (UI, Providers)
│   ├── hooks/               # Custom React hooks (e.g., usePayment)
│   ├── lib/                 # Utility functions, AI schemas, PPTX export logic, x402 validation
│   ├── store/               # Zustand global state management
│   └── types/               # TypeScript interfaces and type definitions
├── .env                     # Environment variables
├── package.json             # Project dependencies and scripts
└── tailwind.config.js       # Tailwind CSS configuration
```

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:
- [Node.js](https://nodejs.org/) (v18 or higher recommended)
- `npm`, `yarn`, `pnpm`, or `bun`

You will also need:
- An Algorand wallet (e.g., Pera Wallet, Defly Wallet)
- An active API key for Google Gemini (Google AI Studio)
- A GitHub API Token (if you wish to use the GitHub repo parsing feature)

## 🚀 Step-by-Step Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd pitchforge-ai
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Set up Environment Variables:**
   Create a `.env.local` file in the root directory (or update the existing `.env`) with the following keys:
   ```env
   GOOGLE_GENERATIVE_AI_API_KEY=your_gemini_api_key_here
   GITHUB_TOKEN=your_github_personal_access_token_here
   ```

4. **Run the Development Server:**
   ```bash
   npm run dev
   ```

5. **Open the Application:**
   Open [http://localhost:3000](http://localhost:3000) in your browser to start using PitchForge AI.

## 📖 How it Works (Implementation Details)

1. **Upload / Connect:** Users begin by uploading a Markdown file or providing a GitHub URL. The `/api/ai/parse` route fetches and extracts the technical data.
2. **AI Consultation:** The app feeds the technical data to Gemini through the AI SDK, assessing technical architecture, target audience, investor intelligence, and presentation strategy.
3. **Generation:** Once the gaps are addressed, the `/api/ai/presentation` endpoint generates the entire slide deck layout, copy, and image prompts.
4. **Payment & Export:** To export the deck, the user pays a microtransaction via Algorand (x402 protocol). The transaction is verified, and the deck is exported to a `.pptx` file using `pptxgenjs`.
