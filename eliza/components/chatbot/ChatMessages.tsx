import ChatBubble from "./ChatBubble"

type Film = {
  title: string
  rating: string
  genre: string
}

type Message = {
  role: "bot" | "user"
  content: string
  films?: Film[]
}

type ChatMessagesProps = {
  messages: Message[]
}

export default function ChatMessages({ messages }: ChatMessagesProps) {
  return (
    <div className="flex-1 overflow-y-auto px-6 py-6 flex flex-col gap-4">
      {messages.map((message, index) => (
        <ChatBubble key={index} {...message} />
      ))}
    </div>
  )
}