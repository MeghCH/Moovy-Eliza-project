import ChatCard from "@/components/search/ChatCard";

const mockChats = [
  {
    id: 1,
    title: "Films d'horreur pour un dimanche",
    date: "Aujourd'hui",
    preview: "Voilà 3 films qui vont te faire frissonner...",
  },
  {
    id: 2,
    title: "Comédie romantique légère",
    date: "Hier",
    preview: "Je te recommande Notting Hill ou Amélie...",
  },
  {
    id: 3,
    title: "Thriller psychologique",
    date: "Il y a 3 jours",
    preview: "Si tu aimes les films qui te font réfléchir...",
  },
  {
    id: 4,
    title: "Film d'action années 90",
    date: "Il y a 5 jours",
    preview: "Les classiques comme Die Hard ou Speed...",
  },
  {
    id: 5,
    title: "Animation japonaise",
    date: "Il y a 1 semaine",
    preview: "Miyazaki est incontournable, commence par...",
  },
];

export default function ChatsPage() {
  return (
    <main className="min-h-screen px-8 py-12 max-w-2xl mx-auto">
      <h1 className="text-white text-3xl font-semibold mb-8">
        Mes discussions
      </h1>
      <div className="flex flex-col gap-3">
        {mockChats.map((chat) => (
          <ChatCard key={chat.id} {...chat} />
        ))}
      </div>
    </main>
  );
}
