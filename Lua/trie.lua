
function getTrieNode() return {children={}, isEnd=false} end

Trie = {}  Trie.__index = Trie

function Trie:new()
  local tr = {}
  setmetatable(tr, Trie)
  tr.root = getTrieNode()
  tr.suggestions = {}
  return tr
end

function Trie:form(...)
  for i, v in ipairs(arg[1]) do
    self:insert(v)
  end
end

function Trie:insert(key)
  node = self.root

  for i=1, #key do
    local c = key:sub(i,i)


    if node.children[c] == nil then
      node.children[c] = getTrieNode()
    end

    node = node.children[c]
    
  end

  node.isEnd = true
  
end

function Trie:suggestionsRec(node, word)
  if node.isEnd then
    self.suggestions[#self.suggestions+1] = word
  end

  for a, n in pairs(node.children) do
    self:suggestionsRec(n, word..a)
  end
end

function Trie:getAutoSugg(key)
  
  self.suggestions = {}
  node = self.root
  
  for i=1, #key do
    local c = key:sub(i,i)
    if node.children[c] == nil then return 0 end
    node = node.children[c]
  end

  if node.children == nil then return -1 end

  self:suggestionsRec(node, key)

  return 1

end
