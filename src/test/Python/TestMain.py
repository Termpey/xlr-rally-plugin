from base64 import b64encode
import CreateFeatureTest, CreateUserStoryTest, UpdateObject

userAndPass = b64encode(b"%s:%s")%("username","password")

featureCTest = CreateFeatureTest(userAndPass)
userStoryCTest = CreateUserStoryTest(userAndPass)
updateObjectTest = UpdateObject(userAndPass)

