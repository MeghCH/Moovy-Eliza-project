"use client";

import { useState } from "react";
import ChatHeader from "@/components/chatbot/ChatHeader";
import ChatMessages from "@/components/chatbot/ChatMessages";
import ChatInput from "@/components/chatbot/ChatInput";

type Film = {
  title: string;
  rating: string;
  genre: string;
};

type Message = {
  role: "bot" | "user";
  content: string;
  films?: Film[];
};

const initialMessages: Message[] = [
  {
    role: "bot",
    content:
      "Salut ! Je suis Movy. Dis-moi ce que tu veux regarder ce soir. Un genre, une ambiance, un acteur… je m'occupe du reste.",
  },
];

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>(initialMessages);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;
    setMessages((prev) => [...prev, { role: "user", content: input }]);
    setInput("");

    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          role: "bot",
          content: "Voilà 3 films qui vont te faire frissonner :",
          films: [
            { title: "Eternal Sunshine", rating: "8.3", genre: "Drame" },
            { title: "Eternal Sunshine", rating: "8.1", genre: "Drame" },
            { title: "Eternal Sunshine", rating: "8.5", genre: "Drame" },
          ],
        },
      ]);
    }, 1000);
  };

  return (
    <div className="flex flex-col h-screen">
      <ChatHeader />
      <ChatMessages messages={messages} />
      <ChatInput input={input} onChange={setInput} onSend={handleSend} />
    </div>
  );
}