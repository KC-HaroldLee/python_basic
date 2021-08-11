module Login
  module_function()
  def checkId(_id)
    members=['nirvana','greenday','offspring']
    for member in members do
      if _id == member
        return true
      end
    end
    return false
  end
end
