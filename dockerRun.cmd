docker run -d ^
  --name reddit-monitor-container ^
  -v "C:\Users\zarif\Documents\GitHub\Reddit-Scraper-with-Push-Notifications\.env:/app/.env" ^
  -v "C:\Users\zarif\Documents\GitHub\Reddit-Scraper-with-Push-Notifications\search.json:/app/search.json" ^
  my-reddit-monitor