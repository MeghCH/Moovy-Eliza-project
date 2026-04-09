export default function Results() {
  const stats = [
    { value: "-60%", description: "de temps pour choisir" },
    { value: "99%", description: "satisfactions utilisateurs" },
    { value: "3x", description: "plus d'engagement" },
  ]

  return (
    <section className="flex flex-col items-center py-24 px-4">
      <h2 className="text-2xl font-bold text-white mb-12">Des résultats concrets</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-4xl">
        {stats.map((stat) => (
          <div
            key={stat.value}
            className="flex flex-col items-center text-center bg-white/5 border border-white/10 rounded-2xl p-8"
          >
            <span className="text-3xl font-semi-bold text-purple-400 mb-2">{stat.value}</span>
            <p className="text-gray-400 text-sm">{stat.description}</p>
          </div>
        ))}
      </div>
    </section>
  )
}