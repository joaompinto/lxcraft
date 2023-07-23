# from lxcraft.path import Directory

DIRNAME = "/run/user/www-data"


# def test_directory_create():
#     Plan("ensure the directory is present", [Directory(DIRNAME)]).run()
#     assert Path(DIRNAME).is_dir()


# def test_directory_remove():
#     Plan(
#         "ensure the user is not present", [Directory(DIRNAME, must_not_exist=True)]
#     ).run()
#     assert not Path(DIRNAME).exists()


# def test_user_mutiple():
#     test_directory_create()
#     test_directory_remove()
