export default function HowItWorks() {
  const steps = [
    { number: 1, title: "Décris ton envie", description: "une ambiance, un genre, une émotion" },
    { number: 2, title: "MooVy analyse", description: "et cherche dans des milliers de films" },
    { number: 3, title: "Tu reçois ta sélection", description: "en quelques secondes, prête à regarder" },
  ]

  return (
    <section className="flex flex-col items-center py-24 px-4">
      <h2 className="text-2xl font-bold text-white mb-12">Comment ça marche</h2>
      <div className="flex flex-col gap-6 w-full max-w-2xl">
        {steps.map((step) => (
          <div key={step.number} className="flex items-center gap-6">
            <span className="flex items-center justify-center w-10 h-10 rounded-full bg-purple-600 text-white font-bold shrink-0">
              {step.number}
            </span>
            <p className="text-white">
              <span className="font-semibold">{step.title}</span>
              <span className="text-gray-400"> : {step.description}</span>
            </p>
          </div>
        ))}
      </div>
    </section>
  )
}