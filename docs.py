from abc import ABC, abstractmethod

'''
DocGenerator(ABC)
Letter(ABC)
Resume(ABC)
FancyLetter(Letter)
FancyResume(Resume)
ModernLetter(Letter)
ModernResume(Resume)
ModernDocGenerator(DocGenerator)
FancyDocGenerator(DocGenerator)
'''
# interfaces


class DocGenerator(ABC):
    @abstractmethod
    def create_letter(self):
        pass

    @abstractmethod
    def create_resume(self):
        pass


class Letter(ABC):
    pass


class Resume(ABC):
    pass

# classes


class FancyLetter(Letter):
    pass


class FancyResume(Resume):
    pass


class ModernLetter(Letter):
    pass


class ModernResume(Letter):
    pass


class FancyDocGenerator(DocGenerator):
    def create_letter(self):
        return FancyLetter()

    def create_resume(self):
        return FancyResume()


class ModernDocGenerator(DocGenerator):
    def create_letter(self):
        return ModernLetter()

    def create_resume(self):
        return ModernResume()
