# email.blog
a flask bloging platform. Listen to an imap folder and then post the messages as blog posts.

## Purpose
I am interested in making blogging fast and easy by using email as the writing interface. Eventually I will use this platform to test out AI powered UI experiments.

## Roadmap --> 1.0 
### Getting the platform off of the ground
1. Convert message subject to blog post title and plain text body to blog post.
2. A or B
  2-A. Build templates and configure static site generator.
  2-B. Build API to serve content to a JAMSTACK client.
3. Integrate markdown and HTML formating from multi-part messages.
4. disply inline images in posts. Display/embed attachments in posts.
5. Configure email clients to use public key encryption. Write or configure module to decrypt messages. Authentication will be via public key encryption.

## Roadmap 1.0 --> 2.0
### AI integration and feature buildout
1. Autofetch links; screenshot, thumbnail and scrape content.
2. Summarize scraped content for thumbnail caption.
3. Read text from images
4. Image auto-tagging
5. Broadcast to other channels.
6. Email listserv
