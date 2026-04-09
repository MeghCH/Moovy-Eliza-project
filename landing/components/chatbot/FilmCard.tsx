type FilmCardProps = {
  title: string
  rating: string
  genre: string
}

export default function FilmCard({ title, rating, genre }: FilmCardProps) {
  return (
    <div className="bg-white/5 border border-white/10 rounded-xl overflow-hidden">
      <div className="w-full h-24 bg-white/10" />
      <div className="p-3 flex flex-col gap-1">
        <p className="text-white text-xs font-medium">{title}</p>
        <p className="text-yellow-500 text-xs">★ {rating}</p>
        <span className="text-xs text-gray-400 bg-white/10 rounded-full px-2 py-0.5 w-fit">
          {genre}
        </span>
      </div>
    </div>
  )
}