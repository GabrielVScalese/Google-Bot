class Answer:

  def __init__ (self, title, link, display_link, snippet):
    self.title = title
    self.link = link
    self.display_link = display_link
    self.snippet = snippet
    # self.icon_url = icon_url
  
  def get_title(self):
    return self.title
  
  def get_link (self):
    return self.link

  def get_display_link(self):
    return self.display_link
  
  def get_snippet (self):
    return self.snippet
  
  # def get_icon_url (self):
  #   return self.icon_url