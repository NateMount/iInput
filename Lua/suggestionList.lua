require "trie"

function getsugg(...)

  t = Trie:new()
  t:form(arg)

  word = io.read()

  t:getAutoSugg(word)

  for k, v in pairs(t.suggestions) do
    print(v)
  end
  
end

getsugg("apple", "app", "zombie", "red", "green", "house", "home", "apt", "print", "lua")

