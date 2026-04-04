import Link from "next/link"
import { RiChat1Line } from "@remixicon/react"

type ChatCardProps = {
  id: number
  title: string
  date: string
  preview: string
}

export default function ChatCard({ title, date, preview }: ChatCardProps) {
  return (
    <Link
      href="/chatbot"
      className="flex items-start gap-4 bg-white/5 border border-white/10 rounded-2xl p-4 hover:bg-white/10 transition-colors"
    >
      <div className="w-9 h-9 rounded-full bg-purple-600/20 border border-purple-500/30 flex items-center justify-center shrink-0 mt-0.5">
        <RiChat1Line className="text-purple-400" size={16} />
      </div>
      <div className="flex flex-col gap-1 overflow-hidden">
        <div className="flex items-center justify-between gap-4">
          <p className="text-white text-sm font-medium truncate">{title}</p>
          <span className="text-gray-500 text-xs shrink-0">{date}</span>
        </div>
        <p className="text-gray-400 text-xs truncate">{preview}</p>
      </div>
    </Link>
  )
}