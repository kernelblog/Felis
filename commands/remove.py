import os


def call(self):
    os.system(f"{self.sudo}rm {self.prefix}/bin/felis")
    print("\nFelis was successfully removed\n")
    os.system(f"{self.sudo}rm -r {self.prefix}/share/felis/")