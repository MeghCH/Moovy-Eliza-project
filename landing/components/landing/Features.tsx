import { RiQuestionAnswerLine, RiFocus3Line, RiFlashlightLine } from "@remixicon/react"

export default function Features() {
  const features = [
    {
      icon: <RiQuestionAnswerLine className="text-4xl text-purple-400 mb-4" />,
      title: "Langage naturel",
      description: "Parle comme à un ami",
    },
    {
      icon: <RiFocus3Line className="text-4xl text-purple-400 mb-4" />,
      title: "Précis",
      description: "S'adapte à ton humeur",
    },
    {
      icon: <RiFlashlightLine className="text-4xl text-purple-400 mb-4" />,
      title: "Instantané",
      description: "Résultat en 5 secondes",
    },
  ]

  return (
    <section className="flex flex-col items-center py-24 px-4">
      <h2 className="text-2xl font-bold text-white mb-12">Pourquoi MooVy ?</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-4xl">
        {features.map((feature) => (
          <div
            key={feature.title}
            className="flex flex-col items-center text-center bg-white/5 border border-white/10 rounded-2xl p-8 hover:bg-white/10 transition-colors"
          >
            {feature.icon}
            <h3 className="text-white font-semibold text-lg mb-2">{feature.title}</h3>
            <p className="text-gray-400 text-sm">{feature.description}</p>
          </div>
        ))}
      </div>
    </section>
  )
}