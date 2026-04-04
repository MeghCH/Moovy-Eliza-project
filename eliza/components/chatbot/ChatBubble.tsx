import FilmCard from "./FilmCard"

type Film = {
  title: string
  rating: string
  genre: string
}

type ChatBubbleProps = {
  role: "bot" | "user"
  content: string
  films?: Film[]
}

export default function ChatBubble({ role, content, films }: ChatBubbleProps) {
  return (
    <div className={`flex ${role === "user" ? "justify-end" : "justify-start"} gap-3`}>

      {role === "bot" && (
        <div className="w-8 h-8 rounded-full bg-purple-600 flex items-center justify-center text-white text-xs shrink-0">
          M
        </div>
      )}

      <div className="flex flex-col gap-3 max-w-sm">
        <div className={`px-4 py-3 rounded-2xl text-sm ${
          role === "bot" ? "bg-white/10 text-white" : "bg-purple-600 text-white"
        }`}>
          {content}
        </div>

        {films && (
          <div className="grid grid-cols-3 gap-2">
            {films.map((film, i) => (
              <FilmCard key={i} {...film} />
            ))}
          </div>
        )}
      </div>

    </div>
  )
}