export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-8 bg-background text-foreground">
      <div className="text-center space-y-6">
        <h1 className="text-4xl font-bold tracking-tight sm:text-6xl">
          Welcome to Revo
        </h1>
        <p className="text-lg text-muted-foreground max-w-md mx-auto">
          Your website is now live. Start building something amazing.
        </p>
      </div>
    </main>
  )
}
