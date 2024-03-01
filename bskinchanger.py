import pandas as pd
import os




def replace_row_by_name(csv_file, name_to_find, name_to_replace, changed_columns=None):
    if changed_columns is None:
        changed_columns = []

    # Чтение CSV файла в DataFrame
    df = pd.read_csv(csv_file)

    # Поиск индекса строки для замены
    index_to_replace = df.index[df['Name'] == name_to_find].tolist()
    if not index_to_replace:
        print(f"Строка с именем '{name_to_find}' не найдена.")
        return

    # Поиск индекса строки для вставки
    index_to_insert = df.index[df['Name'] == name_to_replace].tolist()
    if not index_to_insert:
        print(f"Строка с именем '{name_to_replace}' не найдена.")
        return

    # Сохранение значения Name
    original_name = df.loc[index_to_replace, 'Name'].values[0]

    # Замена значений в выбранных столбцах
    for key in changed_columns:
        if key in df.columns:
            df.loc[index_to_replace, key] = df.loc[index_to_insert, key].values[0]
        else:
            print(f"Столбец '{key}' отсутствует в строке для замены.")

    # Восстановление значения Name
    df.loc[index_to_replace, 'Name'] = original_name

    # Перезапись CSV файла с обновленными данными
    df.to_csv(csv_file, index=False)
    print(f"Строка с именем '{name_to_find}' успешно заменена на строку с именем '{name_to_replace}'.")


# Пример использования функции для замены дефолтного скина на нужный (Изменение моделей и анимаций)
def skinchanger(default_skin_name, replace_skin_name):
    replace_row_by_name('skin_confs.csv', default_skin_name, replace_skin_name,
                        ['Model', 'ModelCNOverride', 'GadgetModel', 'PortraitCameraFile', 'MirrorIntro', 'IdleAnim',
                         'WalkAnim', 'PrimarySkillAnim', 'SecondarySkillAnim', 'OverchargeSkillAnim',
                         'PrimarySkillRecoilAnim', 'PrimarySkillRecoilAnim2', 'SecondarySkillRecoilAnim',
                         'SecondarySkillRecoilAnim2', 'ReloadingAnim', 'PushbackAnim', 'DeployAnim', 'HappyAnim',
                         'HappyLoopAnim', 'RecruitRoadOverrideAnim', 'SadAnim', 'SadLoopAnim', 'LobbyAnim',
                         'LobbyLoopAnim', 'HeroScreenIdleAnim', 'HeroScreenAnim', 'HeroScreenLoopAnim', 'SignatureAnim',
                         'GachaOverrideAnim', 'HappyEnterAnim', 'SadEnterAnim', 'ProfileAnim', 'ShopGroupProfileAnim',
                         'BrawlPassPopupProfileAnim', 'IntroAnim', 'EnvAnim', 'BossAutoAttackAnim',
                         'BossAutoAttackRecoilAnim', 'BossAutoAttackRecoilAnim2', 'GadgetActiveAnim',
                         'GadgetRecoilAnim', 'IdleFace', 'WalkFace', 'HappyFace', 'HappyLoopFace',
                         'RecruitRoadOverrideFace', 'SadFace', 'SadLoopFace', 'LobbyFace', 'LobbyLoopFace',
                         'HeroScreenIdleFace', 'HeroScreenFace', 'HeroScreenLoopFace', 'SignatureFace', 'ProfileFace',
                         'IntroFace', 'LobbyEffect', 'HeroScreenEffect', 'SignatureEffect', 'HappyEffect', 'SadEffect',
                         'PetInSameSprite', 'AttackLocksAttackAngle', 'UltiLocksAttackAngle', 'MainAttackProjectile',
                         'MainAttackOverchargedProjectile', 'SecondaryProjectile', 'ThirdProjectile', 'UltiProjectile',
                         'OverchargedUltiProjectile', 'MainAttackEffect', 'MainAttackEffect2', 'UltiAttackEffect',
                         'UltiAttackEffect2', 'OverchargedUltiAttackEffect', 'OverchargedUltiAttackEffect2',
                         'ShieldEffect', 'UseBlueTextureInMenus', 'MainAttackUseEffect', 'UltiUseEffect',
                         'OverchargedUltiUseEffect', 'UltiEndEffect', 'MeleeHitEffect', 'SpawnEffect', 'ReloadEffect',
                         'UltiLoopEffect', 'UltiLoopEffect2', 'OverchargedUltiLoopEffect', 'OverchargedUltiLoopEffect2',
                         'StarPower1Effect', 'StarPower2Effect', 'AreaEffect', 'AreaEffectStarPower',
                         'AreaEffectStarPower2', 'AreaEffectAttack', 'AreaEffectAttack2', 'AreaEffectUlti',
                         'AreaEffectUlti2', 'OverchargedAreaEffectUlti', 'OverchargedAreaEffectUlti2', 'PetrolEffect',
                         'SpawnedItem', 'SpawnedItem2', 'KillCelebrationSoundVO', 'InLeadCelebrationSoundVO',
                         'StartSoundVO', 'UseUltiSoundVO', 'TakeDamageSoundVO', 'DeathSoundVO', 'AttackSoundVO',
                         'UnlockVO', 'UnlockVOIndex', 'BoneEffect1', 'BoneEffectUse1', 'BoneEffect2', 'BoneEffectUse2',
                         'BoneEffect3', 'BoneEffectUse3', 'BoneEffect4', 'BoneEffectUse4', 'BoneEffect5',
                         'BoneEffectUse5', 'BoneEffect6', 'BoneEffectUse6', 'AutoAttackProjectile',
                         'ProjectileForShockyStarPower', 'OverchargedProjectileForShockyStarPower',
                         'IncendiaryStarPowerAreaEffect', 'KillEffect', 'DeathEffect', 'MoveEffect', 'MoveEffect2',
                         'ChargeMoveEffect', 'OverchargedChargeMoveEffect', 'StillEffect', 'StillEffect2',
                         'LoopingEffect', 'ChargedShotEffect', 'DisableHeadRotation', 'PoisonEffect', 'BuffEffect',
                         'AttackBuildUpEffect', 'SpecialMaterialSetup', 'FaceCoversWholeTexture', 'CustomEffect1',
                         'CustomEffect2'])

    # Пример использования функции для замены дефолтного скина на нужный (Изменение текстур)
    replace_row_by_name('skins.csv', default_skin_name, replace_skin_name,
                        ['BlueTexture', 'RedTexture', 'BlueSpecular', 'RedSpecular', 'OutlineShader',
                         'PackOfferAnimOverride', 'BattleIntroXOffset', 'BattleIntroZOffset', 'BattleIntroVFX'])
def push_via_adb():
    os.system("adb push skin_confs.csv /data/user/0/com.supercell.brawlstars/update/csv_logic/")
    os.system("adb push skins.csv /data/user/0/com.supercell.brawlstars/update/csv_logic/")
if __name__ == '__main__':
    default_skin_name = input("Default skin name: ")
    replace_skin_name = input("Replace skin name: ")
    skinchanger(default_skin_name, replace_skin_name)
    push = input("push via adb y/n: ").lower()
    if push == 'y':
        push_via_adb()