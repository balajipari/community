# Product Community UI

A minimal React frontend for the Product Community API, built with Vite, TypeScript, and shadcn/ui.

## Features

- 🤖 AI-powered product ideation chat interface
- 💬 Real-time conversation with AI assistant
- 🎨 Clean, modern UI with shadcn/ui components
- 📱 Responsive design
- 🔄 Conversation history and reset functionality

## Tech Stack

- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite
- **UI Library**: shadcn/ui + Tailwind CSS
- **State Management**: React Context API
- **HTTP Client**: Fetch API
- **Icons**: Lucide React

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Product Community API running on localhost:8000

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```

3. **Open your browser:**
   Navigate to `http://localhost:5173`

### Building for Production

```bash
npm run build
```

## Project Structure

```
src/
├── components/          # UI components
│   ├── ui/            # shadcn/ui components
│   └── ChatInterface.tsx  # Main chat component
├── contexts/           # React contexts
│   └── IdeationContext.tsx  # State management
├── lib/               # Utilities
│   └── api.ts         # API client
├── App.tsx            # Main app component
├── main.tsx           # Entry point
└── globals.css        # Global styles
```

## API Integration

The frontend connects to the Product Community API endpoints:

- `POST /api/ideation/chat` - Send messages to AI
- `POST /api/ideation/reset` - Reset conversation
- `GET /api/ideation/config` - Get API configuration

## Development

- **Hot Reload**: Vite provides instant updates during development
- **TypeScript**: Full type safety for better development experience
- **ESLint**: Code quality and consistency
- **Tailwind CSS**: Utility-first CSS framework

## Customization

- **Themes**: Modify CSS variables in `globals.css`
- **Components**: Add new shadcn/ui components as needed
- **Styling**: Use Tailwind CSS classes for custom styling
