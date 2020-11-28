# email.blog
a flask bloging platform. Listen to an imap folder and then post the messages as blog posts.

## Purpose
I am interested in making blogging fast and easy by using email as the writing interface. Eventually I will use this platform to test out AI powered UI experiments.

## Roadmap --> 1.0 
### Getting the platform off of the ground
1. Convert message subject to blog post title and plain text body to blog post. [x]
~~2. Automatically ~~**
   ~~1. fetch links~~
   ~~2. Screenshot page~~
  ~~3. Thumbnail screenshot and embed in post.~~
  ~~4. Scrape content~~
   ~~5. Save and attribute scraped content~~
   ** I decided to move this to a spereate project for now.
3. Implement tags for posts []
4. Save everything to a Database [x]
5. i or ii
    1. Build templates and ~~configure~~ build a static site generator.[x]
    2. Build API to serve content to a JAMSTACK client.
6. Integrate []markdown and [x]HTML formating from multi-part messages.
7. Disply inline images in posts. Display/embed attachments in posts.[x]
8. Configure email clients to use public key encryption. Write or configure module to decrypt messages. Authentication will be via public key encryption. []

## Roadmap 1.0 --> 2.0
### AI integration and feature buildout
1. Summarize scraped content for thumbnail caption. []
2. Email listserv []
3. Broadcast to other channels. []
4. Image auto-tagging []
5. Read text from images []
