class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        
        self.name = name
        self.pet_type = pet_type
        self._owner = None  # Internal attribute for the owner
        
        if owner:
            self.owner = owner

        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        if not isinstance(new_owner, Owner):
            raise Exception("Invalid owner type")
        
        if self._owner is not None and self in self._owner.pets():
            self._owner.pets().remove(self)

        self._owner = new_owner
        new_owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
        if pet not in self.pets_list:
            self.pets_list.append(pet)
            pet._owner = self

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)