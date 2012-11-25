# $ANTLR 3.4 /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g 2012-11-23 11:29:38

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
AND=4
BODYLBL=5
CBR=6
CHAR=7
CMA=8
COL=9
COMPLBL=10
CONTENTLBL=11
ELSE=12
GAMELBL=13
IDLBL=14
IF=15
LINK=16
MAG=17
MAGLBL=18
MAXLBL=19
MINLBL=20
MOVELBL=21
MOVESLBL=22
NOT=23
NUM=24
OBR=25
OPENLBL=26
ORD=27
ORDLBL=28
OWNERLBL=29
PARTLBL=30
PLAYERLBL=31
ROLELBL=32
RULELBL=33
RULESLBL=34
SCOPELBL=35
SCOPEVAL=36
STAR=37
STORELBL=38
STR=39
STRUCTLBL=40
STRUCTVAL=41
SYM=42
SYSLBL=43
THEN=44
TURNLBL=45
UNDEFLBL=46
VALUE=47
VISLBL=48
VISVAL=49
WS=50

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "AND", "BODYLBL", "CBR", "CHAR", "CMA", "COL", "COMPLBL", "CONTENTLBL", 
    "ELSE", "GAMELBL", "IDLBL", "IF", "LINK", "MAG", "MAGLBL", "MAXLBL", 
    "MINLBL", "MOVELBL", "MOVESLBL", "NOT", "NUM", "OBR", "OPENLBL", "ORD", 
    "ORDLBL", "OWNERLBL", "PARTLBL", "PLAYERLBL", "ROLELBL", "RULELBL", 
    "RULESLBL", "SCOPELBL", "SCOPEVAL", "STAR", "STORELBL", "STR", "STRUCTLBL", 
    "STRUCTVAL", "SYM", "SYSLBL", "THEN", "TURNLBL", "UNDEFLBL", "VALUE", 
    "VISLBL", "VISVAL", "WS"
]




class dgdlParser(Parser):
    grammarFileName = "/Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(dgdlParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class dgdl_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.dgdl_return, self).__init__()

            self.tree = None





    # $ANTLR start "dgdl"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:9:1: dgdl : ( system | game ) EOF ;
    def dgdl(self, ):
        retval = self.dgdl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EOF3 = None
        system1 = None

        game2 = None


        EOF3_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:9:6: ( ( system | game ) EOF )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:9:8: ( system | game ) EOF
                pass 
                root_0 = self._adaptor.nil()


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:9:8: ( system | game )
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == SYSLBL) :
                    alt1 = 1
                elif (LA1_0 == GAMELBL) :
                    alt1 = 2
                else:
                    nvae = NoViableAltException("", 1, 0, self.input)

                    raise nvae


                if alt1 == 1:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:9:9: system
                    pass 
                    self._state.following.append(self.FOLLOW_system_in_dgdl43)
                    system1 = self.system()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, system1.tree)



                elif alt1 == 2:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:9:18: game
                    pass 
                    self._state.following.append(self.FOLLOW_game_in_dgdl47)
                    game2 = self.game()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, game2.tree)





                EOF3 = self.match(self.input, EOF, self.FOLLOW_EOF_in_dgdl50)
                EOF3_tree = self._adaptor.createWithPayload(EOF3)
                self._adaptor.addChild(root_0, EOF3_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "dgdl"


    class system_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.system_return, self).__init__()

            self.tree = None





    # $ANTLR start "system"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:10:1: system : SYSLBL COL OBR id ( CMA game )+ CBR ;
    def system(self, ):
        retval = self.system_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SYSLBL4 = None
        COL5 = None
        OBR6 = None
        CMA8 = None
        CBR10 = None
        id7 = None

        game9 = None


        SYSLBL4_tree = None
        COL5_tree = None
        OBR6_tree = None
        CMA8_tree = None
        CBR10_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:10:8: ( SYSLBL COL OBR id ( CMA game )+ CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:10:10: SYSLBL COL OBR id ( CMA game )+ CBR
                pass 
                root_0 = self._adaptor.nil()


                SYSLBL4 = self.match(self.input, SYSLBL, self.FOLLOW_SYSLBL_in_system57)
                SYSLBL4_tree = self._adaptor.createWithPayload(SYSLBL4)
                self._adaptor.addChild(root_0, SYSLBL4_tree)



                COL5 = self.match(self.input, COL, self.FOLLOW_COL_in_system59)
                COL5_tree = self._adaptor.createWithPayload(COL5)
                self._adaptor.addChild(root_0, COL5_tree)



                OBR6 = self.match(self.input, OBR, self.FOLLOW_OBR_in_system61)
                OBR6_tree = self._adaptor.createWithPayload(OBR6)
                self._adaptor.addChild(root_0, OBR6_tree)



                self._state.following.append(self.FOLLOW_id_in_system63)
                id7 = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, id7.tree)


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:10:28: ( CMA game )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == CMA) :
                        alt2 = 1


                    if alt2 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:10:29: CMA game
                        pass 
                        CMA8 = self.match(self.input, CMA, self.FOLLOW_CMA_in_system66)
                        CMA8_tree = self._adaptor.createWithPayload(CMA8)
                        self._adaptor.addChild(root_0, CMA8_tree)



                        self._state.following.append(self.FOLLOW_game_in_system68)
                        game9 = self.game()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, game9.tree)



                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1


                CBR10 = self.match(self.input, CBR, self.FOLLOW_CBR_in_system72)
                CBR10_tree = self._adaptor.createWithPayload(CBR10)
                self._adaptor.addChild(root_0, CBR10_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "system"


    class id_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.id_return, self).__init__()

            self.tree = None





    # $ANTLR start "id"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:11:1: id : IDLBL COL VALUE ;
    def id(self, ):
        retval = self.id_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IDLBL11 = None
        COL12 = None
        VALUE13 = None

        IDLBL11_tree = None
        COL12_tree = None
        VALUE13_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:11:4: ( IDLBL COL VALUE )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:11:6: IDLBL COL VALUE
                pass 
                root_0 = self._adaptor.nil()


                IDLBL11 = self.match(self.input, IDLBL, self.FOLLOW_IDLBL_in_id79)
                IDLBL11_tree = self._adaptor.createWithPayload(IDLBL11)
                self._adaptor.addChild(root_0, IDLBL11_tree)



                COL12 = self.match(self.input, COL, self.FOLLOW_COL_in_id81)
                COL12_tree = self._adaptor.createWithPayload(COL12)
                self._adaptor.addChild(root_0, COL12_tree)



                VALUE13 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_id83)
                VALUE13_tree = self._adaptor.createWithPayload(VALUE13)
                self._adaptor.addChild(root_0, VALUE13_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "id"


    class game_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.game_return, self).__init__()

            self.tree = None





    # $ANTLR start "game"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:12:1: game : GAMELBL COL OBR id CMA composition ( CMA rules )? CMA moves CBR ;
    def game(self, ):
        retval = self.game_return()
        retval.start = self.input.LT(1)


        root_0 = None

        GAMELBL14 = None
        COL15 = None
        OBR16 = None
        CMA18 = None
        CMA20 = None
        CMA22 = None
        CBR24 = None
        id17 = None

        composition19 = None

        rules21 = None

        moves23 = None


        GAMELBL14_tree = None
        COL15_tree = None
        OBR16_tree = None
        CMA18_tree = None
        CMA20_tree = None
        CMA22_tree = None
        CBR24_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:12:6: ( GAMELBL COL OBR id CMA composition ( CMA rules )? CMA moves CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:12:8: GAMELBL COL OBR id CMA composition ( CMA rules )? CMA moves CBR
                pass 
                root_0 = self._adaptor.nil()


                GAMELBL14 = self.match(self.input, GAMELBL, self.FOLLOW_GAMELBL_in_game91)
                GAMELBL14_tree = self._adaptor.createWithPayload(GAMELBL14)
                self._adaptor.addChild(root_0, GAMELBL14_tree)



                COL15 = self.match(self.input, COL, self.FOLLOW_COL_in_game93)
                COL15_tree = self._adaptor.createWithPayload(COL15)
                self._adaptor.addChild(root_0, COL15_tree)



                OBR16 = self.match(self.input, OBR, self.FOLLOW_OBR_in_game95)
                OBR16_tree = self._adaptor.createWithPayload(OBR16)
                self._adaptor.addChild(root_0, OBR16_tree)



                self._state.following.append(self.FOLLOW_id_in_game97)
                id17 = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, id17.tree)


                CMA18 = self.match(self.input, CMA, self.FOLLOW_CMA_in_game99)
                CMA18_tree = self._adaptor.createWithPayload(CMA18)
                self._adaptor.addChild(root_0, CMA18_tree)



                self._state.following.append(self.FOLLOW_composition_in_game101)
                composition19 = self.composition()

                self._state.following.pop()
                self._adaptor.addChild(root_0, composition19.tree)


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:12:43: ( CMA rules )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == CMA) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == RULESLBL) :
                        alt3 = 1
                if alt3 == 1:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:12:44: CMA rules
                    pass 
                    CMA20 = self.match(self.input, CMA, self.FOLLOW_CMA_in_game104)
                    CMA20_tree = self._adaptor.createWithPayload(CMA20)
                    self._adaptor.addChild(root_0, CMA20_tree)



                    self._state.following.append(self.FOLLOW_rules_in_game106)
                    rules21 = self.rules()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, rules21.tree)





                CMA22 = self.match(self.input, CMA, self.FOLLOW_CMA_in_game110)
                CMA22_tree = self._adaptor.createWithPayload(CMA22)
                self._adaptor.addChild(root_0, CMA22_tree)



                self._state.following.append(self.FOLLOW_moves_in_game112)
                moves23 = self.moves()

                self._state.following.pop()
                self._adaptor.addChild(root_0, moves23.tree)


                CBR24 = self.match(self.input, CBR, self.FOLLOW_CBR_in_game115)
                CBR24_tree = self._adaptor.createWithPayload(CBR24)
                self._adaptor.addChild(root_0, CBR24_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "game"


    class composition_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.composition_return, self).__init__()

            self.tree = None





    # $ANTLR start "composition"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:13:1: composition : COMPLBL COL OBR turns CMA participants ( CMA player )+ ( CMA store )* ( CMA rolelist )? CBR ;
    def composition(self, ):
        retval = self.composition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COMPLBL25 = None
        COL26 = None
        OBR27 = None
        CMA29 = None
        CMA31 = None
        CMA33 = None
        CMA35 = None
        CBR37 = None
        turns28 = None

        participants30 = None

        player32 = None

        store34 = None

        rolelist36 = None


        COMPLBL25_tree = None
        COL26_tree = None
        OBR27_tree = None
        CMA29_tree = None
        CMA31_tree = None
        CMA33_tree = None
        CMA35_tree = None
        CBR37_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:13:13: ( COMPLBL COL OBR turns CMA participants ( CMA player )+ ( CMA store )* ( CMA rolelist )? CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:13:15: COMPLBL COL OBR turns CMA participants ( CMA player )+ ( CMA store )* ( CMA rolelist )? CBR
                pass 
                root_0 = self._adaptor.nil()


                COMPLBL25 = self.match(self.input, COMPLBL, self.FOLLOW_COMPLBL_in_composition123)
                COMPLBL25_tree = self._adaptor.createWithPayload(COMPLBL25)
                self._adaptor.addChild(root_0, COMPLBL25_tree)



                COL26 = self.match(self.input, COL, self.FOLLOW_COL_in_composition125)
                COL26_tree = self._adaptor.createWithPayload(COL26)
                self._adaptor.addChild(root_0, COL26_tree)



                OBR27 = self.match(self.input, OBR, self.FOLLOW_OBR_in_composition127)
                OBR27_tree = self._adaptor.createWithPayload(OBR27)
                self._adaptor.addChild(root_0, OBR27_tree)



                self._state.following.append(self.FOLLOW_turns_in_composition129)
                turns28 = self.turns()

                self._state.following.pop()
                self._adaptor.addChild(root_0, turns28.tree)


                CMA29 = self.match(self.input, CMA, self.FOLLOW_CMA_in_composition131)
                CMA29_tree = self._adaptor.createWithPayload(CMA29)
                self._adaptor.addChild(root_0, CMA29_tree)



                self._state.following.append(self.FOLLOW_participants_in_composition133)
                participants30 = self.participants()

                self._state.following.pop()
                self._adaptor.addChild(root_0, participants30.tree)


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:13:54: ( CMA player )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == CMA) :
                        LA4_1 = self.input.LA(2)

                        if (LA4_1 == PLAYERLBL) :
                            alt4 = 1




                    if alt4 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:13:55: CMA player
                        pass 
                        CMA31 = self.match(self.input, CMA, self.FOLLOW_CMA_in_composition136)
                        CMA31_tree = self._adaptor.createWithPayload(CMA31)
                        self._adaptor.addChild(root_0, CMA31_tree)



                        self._state.following.append(self.FOLLOW_player_in_composition138)
                        player32 = self.player()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, player32.tree)



                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:13:68: ( CMA store )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == CMA) :
                        LA5_1 = self.input.LA(2)

                        if (LA5_1 == STORELBL) :
                            alt5 = 1




                    if alt5 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:13:69: CMA store
                        pass 
                        CMA33 = self.match(self.input, CMA, self.FOLLOW_CMA_in_composition143)
                        CMA33_tree = self._adaptor.createWithPayload(CMA33)
                        self._adaptor.addChild(root_0, CMA33_tree)



                        self._state.following.append(self.FOLLOW_store_in_composition145)
                        store34 = self.store()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, store34.tree)



                    else:
                        break #loop5


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:13:81: ( CMA rolelist )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == CMA) :
                    alt6 = 1
                if alt6 == 1:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:13:82: CMA rolelist
                    pass 
                    CMA35 = self.match(self.input, CMA, self.FOLLOW_CMA_in_composition150)
                    CMA35_tree = self._adaptor.createWithPayload(CMA35)
                    self._adaptor.addChild(root_0, CMA35_tree)



                    self._state.following.append(self.FOLLOW_rolelist_in_composition152)
                    rolelist36 = self.rolelist()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, rolelist36.tree)





                CBR37 = self.match(self.input, CBR, self.FOLLOW_CBR_in_composition156)
                CBR37_tree = self._adaptor.createWithPayload(CBR37)
                self._adaptor.addChild(root_0, CBR37_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "composition"


    class turns_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.turns_return, self).__init__()

            self.tree = None





    # $ANTLR start "turns"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:14:1: turns : TURNLBL COL OBR MAGLBL COL MAG CMA ORDLBL COL ORD ( CMA MAXLBL COL NUM )? CBR ;
    def turns(self, ):
        retval = self.turns_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TURNLBL38 = None
        COL39 = None
        OBR40 = None
        MAGLBL41 = None
        COL42 = None
        MAG43 = None
        CMA44 = None
        ORDLBL45 = None
        COL46 = None
        ORD47 = None
        CMA48 = None
        MAXLBL49 = None
        COL50 = None
        NUM51 = None
        CBR52 = None

        TURNLBL38_tree = None
        COL39_tree = None
        OBR40_tree = None
        MAGLBL41_tree = None
        COL42_tree = None
        MAG43_tree = None
        CMA44_tree = None
        ORDLBL45_tree = None
        COL46_tree = None
        ORD47_tree = None
        CMA48_tree = None
        MAXLBL49_tree = None
        COL50_tree = None
        NUM51_tree = None
        CBR52_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:14:7: ( TURNLBL COL OBR MAGLBL COL MAG CMA ORDLBL COL ORD ( CMA MAXLBL COL NUM )? CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:14:9: TURNLBL COL OBR MAGLBL COL MAG CMA ORDLBL COL ORD ( CMA MAXLBL COL NUM )? CBR
                pass 
                root_0 = self._adaptor.nil()


                TURNLBL38 = self.match(self.input, TURNLBL, self.FOLLOW_TURNLBL_in_turns164)
                TURNLBL38_tree = self._adaptor.createWithPayload(TURNLBL38)
                self._adaptor.addChild(root_0, TURNLBL38_tree)



                COL39 = self.match(self.input, COL, self.FOLLOW_COL_in_turns166)
                COL39_tree = self._adaptor.createWithPayload(COL39)
                self._adaptor.addChild(root_0, COL39_tree)



                OBR40 = self.match(self.input, OBR, self.FOLLOW_OBR_in_turns168)
                OBR40_tree = self._adaptor.createWithPayload(OBR40)
                self._adaptor.addChild(root_0, OBR40_tree)



                MAGLBL41 = self.match(self.input, MAGLBL, self.FOLLOW_MAGLBL_in_turns171)
                MAGLBL41_tree = self._adaptor.createWithPayload(MAGLBL41)
                self._adaptor.addChild(root_0, MAGLBL41_tree)



                COL42 = self.match(self.input, COL, self.FOLLOW_COL_in_turns173)
                COL42_tree = self._adaptor.createWithPayload(COL42)
                self._adaptor.addChild(root_0, COL42_tree)



                MAG43 = self.match(self.input, MAG, self.FOLLOW_MAG_in_turns175)
                MAG43_tree = self._adaptor.createWithPayload(MAG43)
                self._adaptor.addChild(root_0, MAG43_tree)



                CMA44 = self.match(self.input, CMA, self.FOLLOW_CMA_in_turns177)
                CMA44_tree = self._adaptor.createWithPayload(CMA44)
                self._adaptor.addChild(root_0, CMA44_tree)



                ORDLBL45 = self.match(self.input, ORDLBL, self.FOLLOW_ORDLBL_in_turns179)
                ORDLBL45_tree = self._adaptor.createWithPayload(ORDLBL45)
                self._adaptor.addChild(root_0, ORDLBL45_tree)



                COL46 = self.match(self.input, COL, self.FOLLOW_COL_in_turns181)
                COL46_tree = self._adaptor.createWithPayload(COL46)
                self._adaptor.addChild(root_0, COL46_tree)



                ORD47 = self.match(self.input, ORD, self.FOLLOW_ORD_in_turns183)
                ORD47_tree = self._adaptor.createWithPayload(ORD47)
                self._adaptor.addChild(root_0, ORD47_tree)



                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:14:60: ( CMA MAXLBL COL NUM )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == CMA) :
                    alt7 = 1
                if alt7 == 1:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:14:61: CMA MAXLBL COL NUM
                    pass 
                    CMA48 = self.match(self.input, CMA, self.FOLLOW_CMA_in_turns186)
                    CMA48_tree = self._adaptor.createWithPayload(CMA48)
                    self._adaptor.addChild(root_0, CMA48_tree)



                    MAXLBL49 = self.match(self.input, MAXLBL, self.FOLLOW_MAXLBL_in_turns188)
                    MAXLBL49_tree = self._adaptor.createWithPayload(MAXLBL49)
                    self._adaptor.addChild(root_0, MAXLBL49_tree)



                    COL50 = self.match(self.input, COL, self.FOLLOW_COL_in_turns190)
                    COL50_tree = self._adaptor.createWithPayload(COL50)
                    self._adaptor.addChild(root_0, COL50_tree)



                    NUM51 = self.match(self.input, NUM, self.FOLLOW_NUM_in_turns192)
                    NUM51_tree = self._adaptor.createWithPayload(NUM51)
                    self._adaptor.addChild(root_0, NUM51_tree)






                CBR52 = self.match(self.input, CBR, self.FOLLOW_CBR_in_turns196)
                CBR52_tree = self._adaptor.createWithPayload(CBR52)
                self._adaptor.addChild(root_0, CBR52_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "turns"


    class participants_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.participants_return, self).__init__()

            self.tree = None





    # $ANTLR start "participants"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:15:1: participants : PARTLBL COL OBR MINLBL COL NUM CMA MAXLBL COL ( NUM | UNDEFLBL ) CBR ;
    def participants(self, ):
        retval = self.participants_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PARTLBL53 = None
        COL54 = None
        OBR55 = None
        MINLBL56 = None
        COL57 = None
        NUM58 = None
        CMA59 = None
        MAXLBL60 = None
        COL61 = None
        set62 = None
        CBR63 = None

        PARTLBL53_tree = None
        COL54_tree = None
        OBR55_tree = None
        MINLBL56_tree = None
        COL57_tree = None
        NUM58_tree = None
        CMA59_tree = None
        MAXLBL60_tree = None
        COL61_tree = None
        set62_tree = None
        CBR63_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:15:14: ( PARTLBL COL OBR MINLBL COL NUM CMA MAXLBL COL ( NUM | UNDEFLBL ) CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:15:16: PARTLBL COL OBR MINLBL COL NUM CMA MAXLBL COL ( NUM | UNDEFLBL ) CBR
                pass 
                root_0 = self._adaptor.nil()


                PARTLBL53 = self.match(self.input, PARTLBL, self.FOLLOW_PARTLBL_in_participants204)
                PARTLBL53_tree = self._adaptor.createWithPayload(PARTLBL53)
                self._adaptor.addChild(root_0, PARTLBL53_tree)



                COL54 = self.match(self.input, COL, self.FOLLOW_COL_in_participants206)
                COL54_tree = self._adaptor.createWithPayload(COL54)
                self._adaptor.addChild(root_0, COL54_tree)



                OBR55 = self.match(self.input, OBR, self.FOLLOW_OBR_in_participants208)
                OBR55_tree = self._adaptor.createWithPayload(OBR55)
                self._adaptor.addChild(root_0, OBR55_tree)



                MINLBL56 = self.match(self.input, MINLBL, self.FOLLOW_MINLBL_in_participants210)
                MINLBL56_tree = self._adaptor.createWithPayload(MINLBL56)
                self._adaptor.addChild(root_0, MINLBL56_tree)



                COL57 = self.match(self.input, COL, self.FOLLOW_COL_in_participants212)
                COL57_tree = self._adaptor.createWithPayload(COL57)
                self._adaptor.addChild(root_0, COL57_tree)



                NUM58 = self.match(self.input, NUM, self.FOLLOW_NUM_in_participants214)
                NUM58_tree = self._adaptor.createWithPayload(NUM58)
                self._adaptor.addChild(root_0, NUM58_tree)



                CMA59 = self.match(self.input, CMA, self.FOLLOW_CMA_in_participants217)
                CMA59_tree = self._adaptor.createWithPayload(CMA59)
                self._adaptor.addChild(root_0, CMA59_tree)



                MAXLBL60 = self.match(self.input, MAXLBL, self.FOLLOW_MAXLBL_in_participants219)
                MAXLBL60_tree = self._adaptor.createWithPayload(MAXLBL60)
                self._adaptor.addChild(root_0, MAXLBL60_tree)



                COL61 = self.match(self.input, COL, self.FOLLOW_COL_in_participants221)
                COL61_tree = self._adaptor.createWithPayload(COL61)
                self._adaptor.addChild(root_0, COL61_tree)



                set62 = self.input.LT(1)

                if self.input.LA(1) == NUM or self.input.LA(1) == UNDEFLBL:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set62))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                CBR63 = self.match(self.input, CBR, self.FOLLOW_CBR_in_participants229)
                CBR63_tree = self._adaptor.createWithPayload(CBR63)
                self._adaptor.addChild(root_0, CBR63_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "participants"


    class player_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.player_return, self).__init__()

            self.tree = None





    # $ANTLR start "player"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:16:1: player : PLAYERLBL COL OBR id ( CMA roles )? CBR ;
    def player(self, ):
        retval = self.player_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PLAYERLBL64 = None
        COL65 = None
        OBR66 = None
        CMA68 = None
        CBR70 = None
        id67 = None

        roles69 = None


        PLAYERLBL64_tree = None
        COL65_tree = None
        OBR66_tree = None
        CMA68_tree = None
        CBR70_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:16:8: ( PLAYERLBL COL OBR id ( CMA roles )? CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:16:10: PLAYERLBL COL OBR id ( CMA roles )? CBR
                pass 
                root_0 = self._adaptor.nil()


                PLAYERLBL64 = self.match(self.input, PLAYERLBL, self.FOLLOW_PLAYERLBL_in_player236)
                PLAYERLBL64_tree = self._adaptor.createWithPayload(PLAYERLBL64)
                self._adaptor.addChild(root_0, PLAYERLBL64_tree)



                COL65 = self.match(self.input, COL, self.FOLLOW_COL_in_player238)
                COL65_tree = self._adaptor.createWithPayload(COL65)
                self._adaptor.addChild(root_0, COL65_tree)



                OBR66 = self.match(self.input, OBR, self.FOLLOW_OBR_in_player240)
                OBR66_tree = self._adaptor.createWithPayload(OBR66)
                self._adaptor.addChild(root_0, OBR66_tree)



                self._state.following.append(self.FOLLOW_id_in_player242)
                id67 = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, id67.tree)


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:16:31: ( CMA roles )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == CMA) :
                    alt8 = 1
                if alt8 == 1:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:16:32: CMA roles
                    pass 
                    CMA68 = self.match(self.input, CMA, self.FOLLOW_CMA_in_player245)
                    CMA68_tree = self._adaptor.createWithPayload(CMA68)
                    self._adaptor.addChild(root_0, CMA68_tree)



                    self._state.following.append(self.FOLLOW_roles_in_player247)
                    roles69 = self.roles()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, roles69.tree)





                CBR70 = self.match(self.input, CBR, self.FOLLOW_CBR_in_player251)
                CBR70_tree = self._adaptor.createWithPayload(CBR70)
                self._adaptor.addChild(root_0, CBR70_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "player"


    class roles_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.roles_return, self).__init__()

            self.tree = None





    # $ANTLR start "roles"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:17:1: roles : ROLELBL COL OBR VALUE ( CMA VALUE )* CBR ;
    def roles(self, ):
        retval = self.roles_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ROLELBL71 = None
        COL72 = None
        OBR73 = None
        VALUE74 = None
        CMA75 = None
        VALUE76 = None
        CBR77 = None

        ROLELBL71_tree = None
        COL72_tree = None
        OBR73_tree = None
        VALUE74_tree = None
        CMA75_tree = None
        VALUE76_tree = None
        CBR77_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:17:7: ( ROLELBL COL OBR VALUE ( CMA VALUE )* CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:17:9: ROLELBL COL OBR VALUE ( CMA VALUE )* CBR
                pass 
                root_0 = self._adaptor.nil()


                ROLELBL71 = self.match(self.input, ROLELBL, self.FOLLOW_ROLELBL_in_roles259)
                ROLELBL71_tree = self._adaptor.createWithPayload(ROLELBL71)
                self._adaptor.addChild(root_0, ROLELBL71_tree)



                COL72 = self.match(self.input, COL, self.FOLLOW_COL_in_roles261)
                COL72_tree = self._adaptor.createWithPayload(COL72)
                self._adaptor.addChild(root_0, COL72_tree)



                OBR73 = self.match(self.input, OBR, self.FOLLOW_OBR_in_roles263)
                OBR73_tree = self._adaptor.createWithPayload(OBR73)
                self._adaptor.addChild(root_0, OBR73_tree)



                VALUE74 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_roles265)
                VALUE74_tree = self._adaptor.createWithPayload(VALUE74)
                self._adaptor.addChild(root_0, VALUE74_tree)



                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:17:31: ( CMA VALUE )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == CMA) :
                        alt9 = 1


                    if alt9 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:17:32: CMA VALUE
                        pass 
                        CMA75 = self.match(self.input, CMA, self.FOLLOW_CMA_in_roles268)
                        CMA75_tree = self._adaptor.createWithPayload(CMA75)
                        self._adaptor.addChild(root_0, CMA75_tree)



                        VALUE76 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_roles270)
                        VALUE76_tree = self._adaptor.createWithPayload(VALUE76)
                        self._adaptor.addChild(root_0, VALUE76_tree)




                    else:
                        break #loop9


                CBR77 = self.match(self.input, CBR, self.FOLLOW_CBR_in_roles274)
                CBR77_tree = self._adaptor.createWithPayload(CBR77)
                self._adaptor.addChild(root_0, CBR77_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "roles"


    class store_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.store_return, self).__init__()

            self.tree = None





    # $ANTLR start "store"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:18:1: store : STORELBL COL OBR id CMA owner CMA struct CMA vis CBR ;
    def store(self, ):
        retval = self.store_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STORELBL78 = None
        COL79 = None
        OBR80 = None
        CMA82 = None
        CMA84 = None
        CMA86 = None
        CBR88 = None
        id81 = None

        owner83 = None

        struct85 = None

        vis87 = None


        STORELBL78_tree = None
        COL79_tree = None
        OBR80_tree = None
        CMA82_tree = None
        CMA84_tree = None
        CMA86_tree = None
        CBR88_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:18:7: ( STORELBL COL OBR id CMA owner CMA struct CMA vis CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:18:9: STORELBL COL OBR id CMA owner CMA struct CMA vis CBR
                pass 
                root_0 = self._adaptor.nil()


                STORELBL78 = self.match(self.input, STORELBL, self.FOLLOW_STORELBL_in_store282)
                STORELBL78_tree = self._adaptor.createWithPayload(STORELBL78)
                self._adaptor.addChild(root_0, STORELBL78_tree)



                COL79 = self.match(self.input, COL, self.FOLLOW_COL_in_store284)
                COL79_tree = self._adaptor.createWithPayload(COL79)
                self._adaptor.addChild(root_0, COL79_tree)



                OBR80 = self.match(self.input, OBR, self.FOLLOW_OBR_in_store286)
                OBR80_tree = self._adaptor.createWithPayload(OBR80)
                self._adaptor.addChild(root_0, OBR80_tree)



                self._state.following.append(self.FOLLOW_id_in_store288)
                id81 = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, id81.tree)


                CMA82 = self.match(self.input, CMA, self.FOLLOW_CMA_in_store290)
                CMA82_tree = self._adaptor.createWithPayload(CMA82)
                self._adaptor.addChild(root_0, CMA82_tree)



                self._state.following.append(self.FOLLOW_owner_in_store292)
                owner83 = self.owner()

                self._state.following.pop()
                self._adaptor.addChild(root_0, owner83.tree)


                CMA84 = self.match(self.input, CMA, self.FOLLOW_CMA_in_store294)
                CMA84_tree = self._adaptor.createWithPayload(CMA84)
                self._adaptor.addChild(root_0, CMA84_tree)



                self._state.following.append(self.FOLLOW_struct_in_store296)
                struct85 = self.struct()

                self._state.following.pop()
                self._adaptor.addChild(root_0, struct85.tree)


                CMA86 = self.match(self.input, CMA, self.FOLLOW_CMA_in_store298)
                CMA86_tree = self._adaptor.createWithPayload(CMA86)
                self._adaptor.addChild(root_0, CMA86_tree)



                self._state.following.append(self.FOLLOW_vis_in_store300)
                vis87 = self.vis()

                self._state.following.pop()
                self._adaptor.addChild(root_0, vis87.tree)


                CBR88 = self.match(self.input, CBR, self.FOLLOW_CBR_in_store302)
                CBR88_tree = self._adaptor.createWithPayload(CBR88)
                self._adaptor.addChild(root_0, CBR88_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "store"


    class owner_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.owner_return, self).__init__()

            self.tree = None





    # $ANTLR start "owner"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:19:1: owner : OWNERLBL COL OBR VALUE ( CMA VALUE )* CBR ;
    def owner(self, ):
        retval = self.owner_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OWNERLBL89 = None
        COL90 = None
        OBR91 = None
        VALUE92 = None
        CMA93 = None
        VALUE94 = None
        CBR95 = None

        OWNERLBL89_tree = None
        COL90_tree = None
        OBR91_tree = None
        VALUE92_tree = None
        CMA93_tree = None
        VALUE94_tree = None
        CBR95_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:19:7: ( OWNERLBL COL OBR VALUE ( CMA VALUE )* CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:19:9: OWNERLBL COL OBR VALUE ( CMA VALUE )* CBR
                pass 
                root_0 = self._adaptor.nil()


                OWNERLBL89 = self.match(self.input, OWNERLBL, self.FOLLOW_OWNERLBL_in_owner309)
                OWNERLBL89_tree = self._adaptor.createWithPayload(OWNERLBL89)
                self._adaptor.addChild(root_0, OWNERLBL89_tree)



                COL90 = self.match(self.input, COL, self.FOLLOW_COL_in_owner311)
                COL90_tree = self._adaptor.createWithPayload(COL90)
                self._adaptor.addChild(root_0, COL90_tree)



                OBR91 = self.match(self.input, OBR, self.FOLLOW_OBR_in_owner313)
                OBR91_tree = self._adaptor.createWithPayload(OBR91)
                self._adaptor.addChild(root_0, OBR91_tree)



                VALUE92 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_owner315)
                VALUE92_tree = self._adaptor.createWithPayload(VALUE92)
                self._adaptor.addChild(root_0, VALUE92_tree)



                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:19:32: ( CMA VALUE )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == CMA) :
                        alt10 = 1


                    if alt10 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:19:33: CMA VALUE
                        pass 
                        CMA93 = self.match(self.input, CMA, self.FOLLOW_CMA_in_owner318)
                        CMA93_tree = self._adaptor.createWithPayload(CMA93)
                        self._adaptor.addChild(root_0, CMA93_tree)



                        VALUE94 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_owner320)
                        VALUE94_tree = self._adaptor.createWithPayload(VALUE94)
                        self._adaptor.addChild(root_0, VALUE94_tree)




                    else:
                        break #loop10


                CBR95 = self.match(self.input, CBR, self.FOLLOW_CBR_in_owner324)
                CBR95_tree = self._adaptor.createWithPayload(CBR95)
                self._adaptor.addChild(root_0, CBR95_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "owner"


    class struct_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.struct_return, self).__init__()

            self.tree = None





    # $ANTLR start "struct"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:20:1: struct : STRUCTLBL COL STRUCTVAL ;
    def struct(self, ):
        retval = self.struct_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STRUCTLBL96 = None
        COL97 = None
        STRUCTVAL98 = None

        STRUCTLBL96_tree = None
        COL97_tree = None
        STRUCTVAL98_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:20:8: ( STRUCTLBL COL STRUCTVAL )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:20:10: STRUCTLBL COL STRUCTVAL
                pass 
                root_0 = self._adaptor.nil()


                STRUCTLBL96 = self.match(self.input, STRUCTLBL, self.FOLLOW_STRUCTLBL_in_struct331)
                STRUCTLBL96_tree = self._adaptor.createWithPayload(STRUCTLBL96)
                self._adaptor.addChild(root_0, STRUCTLBL96_tree)



                COL97 = self.match(self.input, COL, self.FOLLOW_COL_in_struct333)
                COL97_tree = self._adaptor.createWithPayload(COL97)
                self._adaptor.addChild(root_0, COL97_tree)



                STRUCTVAL98 = self.match(self.input, STRUCTVAL, self.FOLLOW_STRUCTVAL_in_struct335)
                STRUCTVAL98_tree = self._adaptor.createWithPayload(STRUCTVAL98)
                self._adaptor.addChild(root_0, STRUCTVAL98_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "struct"


    class vis_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.vis_return, self).__init__()

            self.tree = None





    # $ANTLR start "vis"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:21:1: vis : VISLBL COL VISVAL ;
    def vis(self, ):
        retval = self.vis_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VISLBL99 = None
        COL100 = None
        VISVAL101 = None

        VISLBL99_tree = None
        COL100_tree = None
        VISVAL101_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:21:5: ( VISLBL COL VISVAL )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:21:7: VISLBL COL VISVAL
                pass 
                root_0 = self._adaptor.nil()


                VISLBL99 = self.match(self.input, VISLBL, self.FOLLOW_VISLBL_in_vis342)
                VISLBL99_tree = self._adaptor.createWithPayload(VISLBL99)
                self._adaptor.addChild(root_0, VISLBL99_tree)



                COL100 = self.match(self.input, COL, self.FOLLOW_COL_in_vis344)
                COL100_tree = self._adaptor.createWithPayload(COL100)
                self._adaptor.addChild(root_0, COL100_tree)



                VISVAL101 = self.match(self.input, VISVAL, self.FOLLOW_VISVAL_in_vis346)
                VISVAL101_tree = self._adaptor.createWithPayload(VISVAL101)
                self._adaptor.addChild(root_0, VISVAL101_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "vis"


    class rolelist_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.rolelist_return, self).__init__()

            self.tree = None





    # $ANTLR start "rolelist"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:22:1: rolelist : ROLELBL COL OBR VALUE ( CMA VALUE )* CBR ;
    def rolelist(self, ):
        retval = self.rolelist_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ROLELBL102 = None
        COL103 = None
        OBR104 = None
        VALUE105 = None
        CMA106 = None
        VALUE107 = None
        CBR108 = None

        ROLELBL102_tree = None
        COL103_tree = None
        OBR104_tree = None
        VALUE105_tree = None
        CMA106_tree = None
        VALUE107_tree = None
        CBR108_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:22:10: ( ROLELBL COL OBR VALUE ( CMA VALUE )* CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:22:12: ROLELBL COL OBR VALUE ( CMA VALUE )* CBR
                pass 
                root_0 = self._adaptor.nil()


                ROLELBL102 = self.match(self.input, ROLELBL, self.FOLLOW_ROLELBL_in_rolelist353)
                ROLELBL102_tree = self._adaptor.createWithPayload(ROLELBL102)
                self._adaptor.addChild(root_0, ROLELBL102_tree)



                COL103 = self.match(self.input, COL, self.FOLLOW_COL_in_rolelist355)
                COL103_tree = self._adaptor.createWithPayload(COL103)
                self._adaptor.addChild(root_0, COL103_tree)



                OBR104 = self.match(self.input, OBR, self.FOLLOW_OBR_in_rolelist357)
                OBR104_tree = self._adaptor.createWithPayload(OBR104)
                self._adaptor.addChild(root_0, OBR104_tree)



                VALUE105 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_rolelist359)
                VALUE105_tree = self._adaptor.createWithPayload(VALUE105)
                self._adaptor.addChild(root_0, VALUE105_tree)



                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:22:34: ( CMA VALUE )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == CMA) :
                        alt11 = 1


                    if alt11 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:22:35: CMA VALUE
                        pass 
                        CMA106 = self.match(self.input, CMA, self.FOLLOW_CMA_in_rolelist362)
                        CMA106_tree = self._adaptor.createWithPayload(CMA106)
                        self._adaptor.addChild(root_0, CMA106_tree)



                        VALUE107 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_rolelist364)
                        VALUE107_tree = self._adaptor.createWithPayload(VALUE107)
                        self._adaptor.addChild(root_0, VALUE107_tree)




                    else:
                        break #loop11


                CBR108 = self.match(self.input, CBR, self.FOLLOW_CBR_in_rolelist368)
                CBR108_tree = self._adaptor.createWithPayload(CBR108)
                self._adaptor.addChild(root_0, CBR108_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "rolelist"


    class rules_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.rules_return, self).__init__()

            self.tree = None





    # $ANTLR start "rules"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:23:1: rules : RULESLBL COL OBR rule ( CMA rule )* CBR ;
    def rules(self, ):
        retval = self.rules_return()
        retval.start = self.input.LT(1)


        root_0 = None

        RULESLBL109 = None
        COL110 = None
        OBR111 = None
        CMA113 = None
        CBR115 = None
        rule112 = None

        rule114 = None


        RULESLBL109_tree = None
        COL110_tree = None
        OBR111_tree = None
        CMA113_tree = None
        CBR115_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:23:7: ( RULESLBL COL OBR rule ( CMA rule )* CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:23:9: RULESLBL COL OBR rule ( CMA rule )* CBR
                pass 
                root_0 = self._adaptor.nil()


                RULESLBL109 = self.match(self.input, RULESLBL, self.FOLLOW_RULESLBL_in_rules376)
                RULESLBL109_tree = self._adaptor.createWithPayload(RULESLBL109)
                self._adaptor.addChild(root_0, RULESLBL109_tree)



                COL110 = self.match(self.input, COL, self.FOLLOW_COL_in_rules378)
                COL110_tree = self._adaptor.createWithPayload(COL110)
                self._adaptor.addChild(root_0, COL110_tree)



                OBR111 = self.match(self.input, OBR, self.FOLLOW_OBR_in_rules380)
                OBR111_tree = self._adaptor.createWithPayload(OBR111)
                self._adaptor.addChild(root_0, OBR111_tree)



                self._state.following.append(self.FOLLOW_rule_in_rules382)
                rule112 = self.rule()

                self._state.following.pop()
                self._adaptor.addChild(root_0, rule112.tree)


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:23:31: ( CMA rule )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == CMA) :
                        alt12 = 1


                    if alt12 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:23:32: CMA rule
                        pass 
                        CMA113 = self.match(self.input, CMA, self.FOLLOW_CMA_in_rules385)
                        CMA113_tree = self._adaptor.createWithPayload(CMA113)
                        self._adaptor.addChild(root_0, CMA113_tree)



                        self._state.following.append(self.FOLLOW_rule_in_rules387)
                        rule114 = self.rule()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, rule114.tree)



                    else:
                        break #loop12


                CBR115 = self.match(self.input, CBR, self.FOLLOW_CBR_in_rules391)
                CBR115_tree = self._adaptor.createWithPayload(CBR115)
                self._adaptor.addChild(root_0, CBR115_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "rules"


    class rule_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.rule_return, self).__init__()

            self.tree = None





    # $ANTLR start "rule"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:24:1: rule : RULELBL COL OBR id CMA scop CMA body CBR ;
    def rule(self, ):
        retval = self.rule_return()
        retval.start = self.input.LT(1)


        root_0 = None

        RULELBL116 = None
        COL117 = None
        OBR118 = None
        CMA120 = None
        CMA122 = None
        CBR124 = None
        id119 = None

        scop121 = None

        body123 = None


        RULELBL116_tree = None
        COL117_tree = None
        OBR118_tree = None
        CMA120_tree = None
        CMA122_tree = None
        CBR124_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:24:6: ( RULELBL COL OBR id CMA scop CMA body CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:24:8: RULELBL COL OBR id CMA scop CMA body CBR
                pass 
                root_0 = self._adaptor.nil()


                RULELBL116 = self.match(self.input, RULELBL, self.FOLLOW_RULELBL_in_rule399)
                RULELBL116_tree = self._adaptor.createWithPayload(RULELBL116)
                self._adaptor.addChild(root_0, RULELBL116_tree)



                COL117 = self.match(self.input, COL, self.FOLLOW_COL_in_rule401)
                COL117_tree = self._adaptor.createWithPayload(COL117)
                self._adaptor.addChild(root_0, COL117_tree)



                OBR118 = self.match(self.input, OBR, self.FOLLOW_OBR_in_rule403)
                OBR118_tree = self._adaptor.createWithPayload(OBR118)
                self._adaptor.addChild(root_0, OBR118_tree)



                self._state.following.append(self.FOLLOW_id_in_rule405)
                id119 = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, id119.tree)


                CMA120 = self.match(self.input, CMA, self.FOLLOW_CMA_in_rule407)
                CMA120_tree = self._adaptor.createWithPayload(CMA120)
                self._adaptor.addChild(root_0, CMA120_tree)



                self._state.following.append(self.FOLLOW_scop_in_rule409)
                scop121 = self.scop()

                self._state.following.pop()
                self._adaptor.addChild(root_0, scop121.tree)


                CMA122 = self.match(self.input, CMA, self.FOLLOW_CMA_in_rule411)
                CMA122_tree = self._adaptor.createWithPayload(CMA122)
                self._adaptor.addChild(root_0, CMA122_tree)



                self._state.following.append(self.FOLLOW_body_in_rule413)
                body123 = self.body()

                self._state.following.pop()
                self._adaptor.addChild(root_0, body123.tree)


                CBR124 = self.match(self.input, CBR, self.FOLLOW_CBR_in_rule415)
                CBR124_tree = self._adaptor.createWithPayload(CBR124)
                self._adaptor.addChild(root_0, CBR124_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "rule"


    class scop_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.scop_return, self).__init__()

            self.tree = None





    # $ANTLR start "scop"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:25:1: scop : SCOPELBL COL SCOPEVAL ;
    def scop(self, ):
        retval = self.scop_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SCOPELBL125 = None
        COL126 = None
        SCOPEVAL127 = None

        SCOPELBL125_tree = None
        COL126_tree = None
        SCOPEVAL127_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:25:6: ( SCOPELBL COL SCOPEVAL )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:25:8: SCOPELBL COL SCOPEVAL
                pass 
                root_0 = self._adaptor.nil()


                SCOPELBL125 = self.match(self.input, SCOPELBL, self.FOLLOW_SCOPELBL_in_scop423)
                SCOPELBL125_tree = self._adaptor.createWithPayload(SCOPELBL125)
                self._adaptor.addChild(root_0, SCOPELBL125_tree)



                COL126 = self.match(self.input, COL, self.FOLLOW_COL_in_scop425)
                COL126_tree = self._adaptor.createWithPayload(COL126)
                self._adaptor.addChild(root_0, COL126_tree)



                SCOPEVAL127 = self.match(self.input, SCOPEVAL, self.FOLLOW_SCOPEVAL_in_scop427)
                SCOPEVAL127_tree = self._adaptor.createWithPayload(SCOPEVAL127)
                self._adaptor.addChild(root_0, SCOPEVAL127_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "scop"


    class moves_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.moves_return, self).__init__()

            self.tree = None





    # $ANTLR start "moves"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:26:1: moves : MOVESLBL COL OBR move ( CMA move )* CBR ;
    def moves(self, ):
        retval = self.moves_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MOVESLBL128 = None
        COL129 = None
        OBR130 = None
        CMA132 = None
        CBR134 = None
        move131 = None

        move133 = None


        MOVESLBL128_tree = None
        COL129_tree = None
        OBR130_tree = None
        CMA132_tree = None
        CBR134_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:26:7: ( MOVESLBL COL OBR move ( CMA move )* CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:26:9: MOVESLBL COL OBR move ( CMA move )* CBR
                pass 
                root_0 = self._adaptor.nil()


                MOVESLBL128 = self.match(self.input, MOVESLBL, self.FOLLOW_MOVESLBL_in_moves435)
                MOVESLBL128_tree = self._adaptor.createWithPayload(MOVESLBL128)
                self._adaptor.addChild(root_0, MOVESLBL128_tree)



                COL129 = self.match(self.input, COL, self.FOLLOW_COL_in_moves437)
                COL129_tree = self._adaptor.createWithPayload(COL129)
                self._adaptor.addChild(root_0, COL129_tree)



                OBR130 = self.match(self.input, OBR, self.FOLLOW_OBR_in_moves439)
                OBR130_tree = self._adaptor.createWithPayload(OBR130)
                self._adaptor.addChild(root_0, OBR130_tree)



                self._state.following.append(self.FOLLOW_move_in_moves441)
                move131 = self.move()

                self._state.following.pop()
                self._adaptor.addChild(root_0, move131.tree)


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:26:31: ( CMA move )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == CMA) :
                        alt13 = 1


                    if alt13 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:26:32: CMA move
                        pass 
                        CMA132 = self.match(self.input, CMA, self.FOLLOW_CMA_in_moves444)
                        CMA132_tree = self._adaptor.createWithPayload(CMA132)
                        self._adaptor.addChild(root_0, CMA132_tree)



                        self._state.following.append(self.FOLLOW_move_in_moves446)
                        move133 = self.move()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, move133.tree)



                    else:
                        break #loop13


                CBR134 = self.match(self.input, CBR, self.FOLLOW_CBR_in_moves450)
                CBR134_tree = self._adaptor.createWithPayload(CBR134)
                self._adaptor.addChild(root_0, CBR134_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "moves"


    class move_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.move_return, self).__init__()

            self.tree = None





    # $ANTLR start "move"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:27:1: move : MOVELBL COL OBR id ( CMA content )? ( CMA opener )? CMA body CBR ;
    def move(self, ):
        retval = self.move_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MOVELBL135 = None
        COL136 = None
        OBR137 = None
        CMA139 = None
        CMA141 = None
        CMA143 = None
        CBR145 = None
        id138 = None

        content140 = None

        opener142 = None

        body144 = None


        MOVELBL135_tree = None
        COL136_tree = None
        OBR137_tree = None
        CMA139_tree = None
        CMA141_tree = None
        CMA143_tree = None
        CBR145_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:27:6: ( MOVELBL COL OBR id ( CMA content )? ( CMA opener )? CMA body CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:27:8: MOVELBL COL OBR id ( CMA content )? ( CMA opener )? CMA body CBR
                pass 
                root_0 = self._adaptor.nil()


                MOVELBL135 = self.match(self.input, MOVELBL, self.FOLLOW_MOVELBL_in_move458)
                MOVELBL135_tree = self._adaptor.createWithPayload(MOVELBL135)
                self._adaptor.addChild(root_0, MOVELBL135_tree)



                COL136 = self.match(self.input, COL, self.FOLLOW_COL_in_move460)
                COL136_tree = self._adaptor.createWithPayload(COL136)
                self._adaptor.addChild(root_0, COL136_tree)



                OBR137 = self.match(self.input, OBR, self.FOLLOW_OBR_in_move462)
                OBR137_tree = self._adaptor.createWithPayload(OBR137)
                self._adaptor.addChild(root_0, OBR137_tree)



                self._state.following.append(self.FOLLOW_id_in_move464)
                id138 = self.id()

                self._state.following.pop()
                self._adaptor.addChild(root_0, id138.tree)


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:27:27: ( CMA content )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == CMA) :
                    LA14_1 = self.input.LA(2)

                    if (LA14_1 == CONTENTLBL) :
                        alt14 = 1
                if alt14 == 1:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:27:28: CMA content
                    pass 
                    CMA139 = self.match(self.input, CMA, self.FOLLOW_CMA_in_move467)
                    CMA139_tree = self._adaptor.createWithPayload(CMA139)
                    self._adaptor.addChild(root_0, CMA139_tree)



                    self._state.following.append(self.FOLLOW_content_in_move469)
                    content140 = self.content()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, content140.tree)





                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:27:42: ( CMA opener )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == CMA) :
                    LA15_1 = self.input.LA(2)

                    if (LA15_1 == OPENLBL) :
                        alt15 = 1
                if alt15 == 1:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:27:43: CMA opener
                    pass 
                    CMA141 = self.match(self.input, CMA, self.FOLLOW_CMA_in_move474)
                    CMA141_tree = self._adaptor.createWithPayload(CMA141)
                    self._adaptor.addChild(root_0, CMA141_tree)



                    self._state.following.append(self.FOLLOW_opener_in_move476)
                    opener142 = self.opener()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, opener142.tree)





                CMA143 = self.match(self.input, CMA, self.FOLLOW_CMA_in_move480)
                CMA143_tree = self._adaptor.createWithPayload(CMA143)
                self._adaptor.addChild(root_0, CMA143_tree)



                self._state.following.append(self.FOLLOW_body_in_move482)
                body144 = self.body()

                self._state.following.pop()
                self._adaptor.addChild(root_0, body144.tree)


                CBR145 = self.match(self.input, CBR, self.FOLLOW_CBR_in_move484)
                CBR145_tree = self._adaptor.createWithPayload(CBR145)
                self._adaptor.addChild(root_0, CBR145_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "move"


    class content_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.content_return, self).__init__()

            self.tree = None





    # $ANTLR start "content"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:28:1: content : CONTENTLBL COL OBR VALUE ( CMA VALUE )* CBR ;
    def content(self, ):
        retval = self.content_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONTENTLBL146 = None
        COL147 = None
        OBR148 = None
        VALUE149 = None
        CMA150 = None
        VALUE151 = None
        CBR152 = None

        CONTENTLBL146_tree = None
        COL147_tree = None
        OBR148_tree = None
        VALUE149_tree = None
        CMA150_tree = None
        VALUE151_tree = None
        CBR152_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:28:9: ( CONTENTLBL COL OBR VALUE ( CMA VALUE )* CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:28:11: CONTENTLBL COL OBR VALUE ( CMA VALUE )* CBR
                pass 
                root_0 = self._adaptor.nil()


                CONTENTLBL146 = self.match(self.input, CONTENTLBL, self.FOLLOW_CONTENTLBL_in_content492)
                CONTENTLBL146_tree = self._adaptor.createWithPayload(CONTENTLBL146)
                self._adaptor.addChild(root_0, CONTENTLBL146_tree)



                COL147 = self.match(self.input, COL, self.FOLLOW_COL_in_content494)
                COL147_tree = self._adaptor.createWithPayload(COL147)
                self._adaptor.addChild(root_0, COL147_tree)



                OBR148 = self.match(self.input, OBR, self.FOLLOW_OBR_in_content496)
                OBR148_tree = self._adaptor.createWithPayload(OBR148)
                self._adaptor.addChild(root_0, OBR148_tree)



                VALUE149 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_content498)
                VALUE149_tree = self._adaptor.createWithPayload(VALUE149)
                self._adaptor.addChild(root_0, VALUE149_tree)



                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:28:36: ( CMA VALUE )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == CMA) :
                        alt16 = 1


                    if alt16 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:28:37: CMA VALUE
                        pass 
                        CMA150 = self.match(self.input, CMA, self.FOLLOW_CMA_in_content501)
                        CMA150_tree = self._adaptor.createWithPayload(CMA150)
                        self._adaptor.addChild(root_0, CMA150_tree)



                        VALUE151 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_content503)
                        VALUE151_tree = self._adaptor.createWithPayload(VALUE151)
                        self._adaptor.addChild(root_0, VALUE151_tree)




                    else:
                        break #loop16


                CBR152 = self.match(self.input, CBR, self.FOLLOW_CBR_in_content507)
                CBR152_tree = self._adaptor.createWithPayload(CBR152)
                self._adaptor.addChild(root_0, CBR152_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "content"


    class opener_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.opener_return, self).__init__()

            self.tree = None





    # $ANTLR start "opener"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:29:1: opener : OPENLBL COL STR ;
    def opener(self, ):
        retval = self.opener_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPENLBL153 = None
        COL154 = None
        STR155 = None

        OPENLBL153_tree = None
        COL154_tree = None
        STR155_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:29:8: ( OPENLBL COL STR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:29:11: OPENLBL COL STR
                pass 
                root_0 = self._adaptor.nil()


                OPENLBL153 = self.match(self.input, OPENLBL, self.FOLLOW_OPENLBL_in_opener516)
                OPENLBL153_tree = self._adaptor.createWithPayload(OPENLBL153)
                self._adaptor.addChild(root_0, OPENLBL153_tree)



                COL154 = self.match(self.input, COL, self.FOLLOW_COL_in_opener518)
                COL154_tree = self._adaptor.createWithPayload(COL154)
                self._adaptor.addChild(root_0, COL154_tree)



                STR155 = self.match(self.input, STR, self.FOLLOW_STR_in_opener520)
                STR155_tree = self._adaptor.createWithPayload(STR155)
                self._adaptor.addChild(root_0, STR155_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "opener"


    class body_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.body_return, self).__init__()

            self.tree = None





    # $ANTLR start "body"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:30:1: body : ( BODYLBL COL OBR effects ( AND conditional )* CBR | BODYLBL COL OBR conditional ( ELSE conditional )* ( ELSE effects )? CBR );
    def body(self, ):
        retval = self.body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        BODYLBL156 = None
        COL157 = None
        OBR158 = None
        AND160 = None
        CBR162 = None
        BODYLBL163 = None
        COL164 = None
        OBR165 = None
        ELSE167 = None
        ELSE169 = None
        CBR171 = None
        effects159 = None

        conditional161 = None

        conditional166 = None

        conditional168 = None

        effects170 = None


        BODYLBL156_tree = None
        COL157_tree = None
        OBR158_tree = None
        AND160_tree = None
        CBR162_tree = None
        BODYLBL163_tree = None
        COL164_tree = None
        OBR165_tree = None
        ELSE167_tree = None
        ELSE169_tree = None
        CBR171_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:30:6: ( BODYLBL COL OBR effects ( AND conditional )* CBR | BODYLBL COL OBR conditional ( ELSE conditional )* ( ELSE effects )? CBR )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == BODYLBL) :
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == COL) :
                        LA20_2 = self.input.LA(3)

                        if (LA20_2 == OBR) :
                            LA20_3 = self.input.LA(4)

                            if (LA20_3 == VALUE) :
                                alt20 = 1
                            elif (LA20_3 == IF) :
                                alt20 = 2
                            else:
                                nvae = NoViableAltException("", 20, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 20, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 20, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:30:8: BODYLBL COL OBR effects ( AND conditional )* CBR
                    pass 
                    root_0 = self._adaptor.nil()


                    BODYLBL156 = self.match(self.input, BODYLBL, self.FOLLOW_BODYLBL_in_body527)
                    BODYLBL156_tree = self._adaptor.createWithPayload(BODYLBL156)
                    self._adaptor.addChild(root_0, BODYLBL156_tree)



                    COL157 = self.match(self.input, COL, self.FOLLOW_COL_in_body529)
                    COL157_tree = self._adaptor.createWithPayload(COL157)
                    self._adaptor.addChild(root_0, COL157_tree)



                    OBR158 = self.match(self.input, OBR, self.FOLLOW_OBR_in_body531)
                    OBR158_tree = self._adaptor.createWithPayload(OBR158)
                    self._adaptor.addChild(root_0, OBR158_tree)



                    self._state.following.append(self.FOLLOW_effects_in_body533)
                    effects159 = self.effects()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, effects159.tree)


                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:30:32: ( AND conditional )*
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == AND) :
                            alt17 = 1


                        if alt17 == 1:
                            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:30:33: AND conditional
                            pass 
                            AND160 = self.match(self.input, AND, self.FOLLOW_AND_in_body536)
                            AND160_tree = self._adaptor.createWithPayload(AND160)
                            self._adaptor.addChild(root_0, AND160_tree)



                            self._state.following.append(self.FOLLOW_conditional_in_body538)
                            conditional161 = self.conditional()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, conditional161.tree)



                        else:
                            break #loop17


                    CBR162 = self.match(self.input, CBR, self.FOLLOW_CBR_in_body543)
                    CBR162_tree = self._adaptor.createWithPayload(CBR162)
                    self._adaptor.addChild(root_0, CBR162_tree)




                elif alt20 == 2:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:31:4: BODYLBL COL OBR conditional ( ELSE conditional )* ( ELSE effects )? CBR
                    pass 
                    root_0 = self._adaptor.nil()


                    BODYLBL163 = self.match(self.input, BODYLBL, self.FOLLOW_BODYLBL_in_body548)
                    BODYLBL163_tree = self._adaptor.createWithPayload(BODYLBL163)
                    self._adaptor.addChild(root_0, BODYLBL163_tree)



                    COL164 = self.match(self.input, COL, self.FOLLOW_COL_in_body550)
                    COL164_tree = self._adaptor.createWithPayload(COL164)
                    self._adaptor.addChild(root_0, COL164_tree)



                    OBR165 = self.match(self.input, OBR, self.FOLLOW_OBR_in_body552)
                    OBR165_tree = self._adaptor.createWithPayload(OBR165)
                    self._adaptor.addChild(root_0, OBR165_tree)



                    self._state.following.append(self.FOLLOW_conditional_in_body554)
                    conditional166 = self.conditional()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, conditional166.tree)


                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:31:32: ( ELSE conditional )*
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == ELSE) :
                            LA18_1 = self.input.LA(2)

                            if (LA18_1 == IF) :
                                alt18 = 1




                        if alt18 == 1:
                            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:31:33: ELSE conditional
                            pass 
                            ELSE167 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_body557)
                            ELSE167_tree = self._adaptor.createWithPayload(ELSE167)
                            self._adaptor.addChild(root_0, ELSE167_tree)



                            self._state.following.append(self.FOLLOW_conditional_in_body559)
                            conditional168 = self.conditional()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, conditional168.tree)



                        else:
                            break #loop18


                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:31:52: ( ELSE effects )?
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == ELSE) :
                        alt19 = 1
                    if alt19 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:31:53: ELSE effects
                        pass 
                        ELSE169 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_body564)
                        ELSE169_tree = self._adaptor.createWithPayload(ELSE169)
                        self._adaptor.addChild(root_0, ELSE169_tree)



                        self._state.following.append(self.FOLLOW_effects_in_body566)
                        effects170 = self.effects()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, effects170.tree)





                    CBR171 = self.match(self.input, CBR, self.FOLLOW_CBR_in_body570)
                    CBR171_tree = self._adaptor.createWithPayload(CBR171)
                    self._adaptor.addChild(root_0, CBR171_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "body"


    class effects_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.effects_return, self).__init__()

            self.tree = None





    # $ANTLR start "effects"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:32:1: effects : expr ( AND expr )* ;
    def effects(self, ):
        retval = self.effects_return()
        retval.start = self.input.LT(1)


        root_0 = None

        AND173 = None
        expr172 = None

        expr174 = None


        AND173_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:32:9: ( expr ( AND expr )* )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:32:11: expr ( AND expr )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_expr_in_effects577)
                expr172 = self.expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expr172.tree)


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:32:16: ( AND expr )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == AND) :
                        LA21_1 = self.input.LA(2)

                        if (LA21_1 == VALUE) :
                            alt21 = 1




                    if alt21 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:32:17: AND expr
                        pass 
                        AND173 = self.match(self.input, AND, self.FOLLOW_AND_in_effects580)
                        AND173_tree = self._adaptor.createWithPayload(AND173)
                        self._adaptor.addChild(root_0, AND173_tree)



                        self._state.following.append(self.FOLLOW_expr_in_effects582)
                        expr174 = self.expr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, expr174.tree)



                    else:
                        break #loop21




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "effects"


    class conditional_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.conditional_return, self).__init__()

            self.tree = None





    # $ANTLR start "conditional"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:33:1: conditional : IF expr ( AND expr )* THEN effects ;
    def conditional(self, ):
        retval = self.conditional_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF175 = None
        AND177 = None
        THEN179 = None
        expr176 = None

        expr178 = None

        effects180 = None


        IF175_tree = None
        AND177_tree = None
        THEN179_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:33:13: ( IF expr ( AND expr )* THEN effects )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:33:15: IF expr ( AND expr )* THEN effects
                pass 
                root_0 = self._adaptor.nil()


                IF175 = self.match(self.input, IF, self.FOLLOW_IF_in_conditional591)
                IF175_tree = self._adaptor.createWithPayload(IF175)
                self._adaptor.addChild(root_0, IF175_tree)



                self._state.following.append(self.FOLLOW_expr_in_conditional593)
                expr176 = self.expr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, expr176.tree)


                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:33:23: ( AND expr )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == AND) :
                        alt22 = 1


                    if alt22 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:33:24: AND expr
                        pass 
                        AND177 = self.match(self.input, AND, self.FOLLOW_AND_in_conditional596)
                        AND177_tree = self._adaptor.createWithPayload(AND177)
                        self._adaptor.addChild(root_0, AND177_tree)



                        self._state.following.append(self.FOLLOW_expr_in_conditional598)
                        expr178 = self.expr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, expr178.tree)



                    else:
                        break #loop22


                THEN179 = self.match(self.input, THEN, self.FOLLOW_THEN_in_conditional602)
                THEN179_tree = self._adaptor.createWithPayload(THEN179)
                self._adaptor.addChild(root_0, THEN179_tree)



                self._state.following.append(self.FOLLOW_effects_in_conditional604)
                effects180 = self.effects()

                self._state.following.pop()
                self._adaptor.addChild(root_0, effects180.tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "conditional"


    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(dgdlParser.expr_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr"
    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:34:1: expr : VALUE OBR VALUE ( CMA VALUE )* CBR ;
    def expr(self, ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VALUE181 = None
        OBR182 = None
        VALUE183 = None
        CMA184 = None
        VALUE185 = None
        CBR186 = None

        VALUE181_tree = None
        OBR182_tree = None
        VALUE183_tree = None
        CMA184_tree = None
        VALUE185_tree = None
        CBR186_tree = None

        try:
            try:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:34:6: ( VALUE OBR VALUE ( CMA VALUE )* CBR )
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:34:8: VALUE OBR VALUE ( CMA VALUE )* CBR
                pass 
                root_0 = self._adaptor.nil()


                VALUE181 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_expr611)
                VALUE181_tree = self._adaptor.createWithPayload(VALUE181)
                self._adaptor.addChild(root_0, VALUE181_tree)



                OBR182 = self.match(self.input, OBR, self.FOLLOW_OBR_in_expr613)
                OBR182_tree = self._adaptor.createWithPayload(OBR182)
                self._adaptor.addChild(root_0, OBR182_tree)



                VALUE183 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_expr615)
                VALUE183_tree = self._adaptor.createWithPayload(VALUE183)
                self._adaptor.addChild(root_0, VALUE183_tree)



                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:34:24: ( CMA VALUE )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == CMA) :
                        alt23 = 1


                    if alt23 == 1:
                        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:34:25: CMA VALUE
                        pass 
                        CMA184 = self.match(self.input, CMA, self.FOLLOW_CMA_in_expr618)
                        CMA184_tree = self._adaptor.createWithPayload(CMA184)
                        self._adaptor.addChild(root_0, CMA184_tree)



                        VALUE185 = self.match(self.input, VALUE, self.FOLLOW_VALUE_in_expr620)
                        VALUE185_tree = self._adaptor.createWithPayload(VALUE185)
                        self._adaptor.addChild(root_0, VALUE185_tree)




                    else:
                        break #loop23


                CBR186 = self.match(self.input, CBR, self.FOLLOW_CBR_in_expr624)
                CBR186_tree = self._adaptor.createWithPayload(CBR186)
                self._adaptor.addChild(root_0, CBR186_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "expr"



 

    FOLLOW_system_in_dgdl43 = frozenset([])
    FOLLOW_game_in_dgdl47 = frozenset([])
    FOLLOW_EOF_in_dgdl50 = frozenset([1])
    FOLLOW_SYSLBL_in_system57 = frozenset([9])
    FOLLOW_COL_in_system59 = frozenset([25])
    FOLLOW_OBR_in_system61 = frozenset([14])
    FOLLOW_id_in_system63 = frozenset([8])
    FOLLOW_CMA_in_system66 = frozenset([13])
    FOLLOW_game_in_system68 = frozenset([6, 8])
    FOLLOW_CBR_in_system72 = frozenset([1])
    FOLLOW_IDLBL_in_id79 = frozenset([9])
    FOLLOW_COL_in_id81 = frozenset([47])
    FOLLOW_VALUE_in_id83 = frozenset([1])
    FOLLOW_GAMELBL_in_game91 = frozenset([9])
    FOLLOW_COL_in_game93 = frozenset([25])
    FOLLOW_OBR_in_game95 = frozenset([14])
    FOLLOW_id_in_game97 = frozenset([8])
    FOLLOW_CMA_in_game99 = frozenset([10])
    FOLLOW_composition_in_game101 = frozenset([8])
    FOLLOW_CMA_in_game104 = frozenset([34])
    FOLLOW_rules_in_game106 = frozenset([8])
    FOLLOW_CMA_in_game110 = frozenset([22])
    FOLLOW_moves_in_game112 = frozenset([6])
    FOLLOW_CBR_in_game115 = frozenset([1])
    FOLLOW_COMPLBL_in_composition123 = frozenset([9])
    FOLLOW_COL_in_composition125 = frozenset([25])
    FOLLOW_OBR_in_composition127 = frozenset([45])
    FOLLOW_turns_in_composition129 = frozenset([8])
    FOLLOW_CMA_in_composition131 = frozenset([30])
    FOLLOW_participants_in_composition133 = frozenset([8])
    FOLLOW_CMA_in_composition136 = frozenset([31])
    FOLLOW_player_in_composition138 = frozenset([6, 8])
    FOLLOW_CMA_in_composition143 = frozenset([38])
    FOLLOW_store_in_composition145 = frozenset([6, 8])
    FOLLOW_CMA_in_composition150 = frozenset([32])
    FOLLOW_rolelist_in_composition152 = frozenset([6])
    FOLLOW_CBR_in_composition156 = frozenset([1])
    FOLLOW_TURNLBL_in_turns164 = frozenset([9])
    FOLLOW_COL_in_turns166 = frozenset([25])
    FOLLOW_OBR_in_turns168 = frozenset([18])
    FOLLOW_MAGLBL_in_turns171 = frozenset([9])
    FOLLOW_COL_in_turns173 = frozenset([17])
    FOLLOW_MAG_in_turns175 = frozenset([8])
    FOLLOW_CMA_in_turns177 = frozenset([28])
    FOLLOW_ORDLBL_in_turns179 = frozenset([9])
    FOLLOW_COL_in_turns181 = frozenset([27])
    FOLLOW_ORD_in_turns183 = frozenset([6, 8])
    FOLLOW_CMA_in_turns186 = frozenset([19])
    FOLLOW_MAXLBL_in_turns188 = frozenset([9])
    FOLLOW_COL_in_turns190 = frozenset([24])
    FOLLOW_NUM_in_turns192 = frozenset([6])
    FOLLOW_CBR_in_turns196 = frozenset([1])
    FOLLOW_PARTLBL_in_participants204 = frozenset([9])
    FOLLOW_COL_in_participants206 = frozenset([25])
    FOLLOW_OBR_in_participants208 = frozenset([20])
    FOLLOW_MINLBL_in_participants210 = frozenset([9])
    FOLLOW_COL_in_participants212 = frozenset([24])
    FOLLOW_NUM_in_participants214 = frozenset([8])
    FOLLOW_CMA_in_participants217 = frozenset([19])
    FOLLOW_MAXLBL_in_participants219 = frozenset([9])
    FOLLOW_COL_in_participants221 = frozenset([24, 46])
    FOLLOW_set_in_participants223 = frozenset([6])
    FOLLOW_CBR_in_participants229 = frozenset([1])
    FOLLOW_PLAYERLBL_in_player236 = frozenset([9])
    FOLLOW_COL_in_player238 = frozenset([25])
    FOLLOW_OBR_in_player240 = frozenset([14])
    FOLLOW_id_in_player242 = frozenset([6, 8])
    FOLLOW_CMA_in_player245 = frozenset([32])
    FOLLOW_roles_in_player247 = frozenset([6])
    FOLLOW_CBR_in_player251 = frozenset([1])
    FOLLOW_ROLELBL_in_roles259 = frozenset([9])
    FOLLOW_COL_in_roles261 = frozenset([25])
    FOLLOW_OBR_in_roles263 = frozenset([47])
    FOLLOW_VALUE_in_roles265 = frozenset([6, 8])
    FOLLOW_CMA_in_roles268 = frozenset([47])
    FOLLOW_VALUE_in_roles270 = frozenset([6, 8])
    FOLLOW_CBR_in_roles274 = frozenset([1])
    FOLLOW_STORELBL_in_store282 = frozenset([9])
    FOLLOW_COL_in_store284 = frozenset([25])
    FOLLOW_OBR_in_store286 = frozenset([14])
    FOLLOW_id_in_store288 = frozenset([8])
    FOLLOW_CMA_in_store290 = frozenset([29])
    FOLLOW_owner_in_store292 = frozenset([8])
    FOLLOW_CMA_in_store294 = frozenset([40])
    FOLLOW_struct_in_store296 = frozenset([8])
    FOLLOW_CMA_in_store298 = frozenset([48])
    FOLLOW_vis_in_store300 = frozenset([6])
    FOLLOW_CBR_in_store302 = frozenset([1])
    FOLLOW_OWNERLBL_in_owner309 = frozenset([9])
    FOLLOW_COL_in_owner311 = frozenset([25])
    FOLLOW_OBR_in_owner313 = frozenset([47])
    FOLLOW_VALUE_in_owner315 = frozenset([6, 8])
    FOLLOW_CMA_in_owner318 = frozenset([47])
    FOLLOW_VALUE_in_owner320 = frozenset([6, 8])
    FOLLOW_CBR_in_owner324 = frozenset([1])
    FOLLOW_STRUCTLBL_in_struct331 = frozenset([9])
    FOLLOW_COL_in_struct333 = frozenset([41])
    FOLLOW_STRUCTVAL_in_struct335 = frozenset([1])
    FOLLOW_VISLBL_in_vis342 = frozenset([9])
    FOLLOW_COL_in_vis344 = frozenset([49])
    FOLLOW_VISVAL_in_vis346 = frozenset([1])
    FOLLOW_ROLELBL_in_rolelist353 = frozenset([9])
    FOLLOW_COL_in_rolelist355 = frozenset([25])
    FOLLOW_OBR_in_rolelist357 = frozenset([47])
    FOLLOW_VALUE_in_rolelist359 = frozenset([6, 8])
    FOLLOW_CMA_in_rolelist362 = frozenset([47])
    FOLLOW_VALUE_in_rolelist364 = frozenset([6, 8])
    FOLLOW_CBR_in_rolelist368 = frozenset([1])
    FOLLOW_RULESLBL_in_rules376 = frozenset([9])
    FOLLOW_COL_in_rules378 = frozenset([25])
    FOLLOW_OBR_in_rules380 = frozenset([33])
    FOLLOW_rule_in_rules382 = frozenset([6, 8])
    FOLLOW_CMA_in_rules385 = frozenset([33])
    FOLLOW_rule_in_rules387 = frozenset([6, 8])
    FOLLOW_CBR_in_rules391 = frozenset([1])
    FOLLOW_RULELBL_in_rule399 = frozenset([9])
    FOLLOW_COL_in_rule401 = frozenset([25])
    FOLLOW_OBR_in_rule403 = frozenset([14])
    FOLLOW_id_in_rule405 = frozenset([8])
    FOLLOW_CMA_in_rule407 = frozenset([35])
    FOLLOW_scop_in_rule409 = frozenset([8])
    FOLLOW_CMA_in_rule411 = frozenset([5])
    FOLLOW_body_in_rule413 = frozenset([6])
    FOLLOW_CBR_in_rule415 = frozenset([1])
    FOLLOW_SCOPELBL_in_scop423 = frozenset([9])
    FOLLOW_COL_in_scop425 = frozenset([36])
    FOLLOW_SCOPEVAL_in_scop427 = frozenset([1])
    FOLLOW_MOVESLBL_in_moves435 = frozenset([9])
    FOLLOW_COL_in_moves437 = frozenset([25])
    FOLLOW_OBR_in_moves439 = frozenset([21])
    FOLLOW_move_in_moves441 = frozenset([6, 8])
    FOLLOW_CMA_in_moves444 = frozenset([21])
    FOLLOW_move_in_moves446 = frozenset([6, 8])
    FOLLOW_CBR_in_moves450 = frozenset([1])
    FOLLOW_MOVELBL_in_move458 = frozenset([9])
    FOLLOW_COL_in_move460 = frozenset([25])
    FOLLOW_OBR_in_move462 = frozenset([14])
    FOLLOW_id_in_move464 = frozenset([8])
    FOLLOW_CMA_in_move467 = frozenset([11])
    FOLLOW_content_in_move469 = frozenset([8])
    FOLLOW_CMA_in_move474 = frozenset([26])
    FOLLOW_opener_in_move476 = frozenset([8])
    FOLLOW_CMA_in_move480 = frozenset([5])
    FOLLOW_body_in_move482 = frozenset([6])
    FOLLOW_CBR_in_move484 = frozenset([1])
    FOLLOW_CONTENTLBL_in_content492 = frozenset([9])
    FOLLOW_COL_in_content494 = frozenset([25])
    FOLLOW_OBR_in_content496 = frozenset([47])
    FOLLOW_VALUE_in_content498 = frozenset([6, 8])
    FOLLOW_CMA_in_content501 = frozenset([47])
    FOLLOW_VALUE_in_content503 = frozenset([6, 8])
    FOLLOW_CBR_in_content507 = frozenset([1])
    FOLLOW_OPENLBL_in_opener516 = frozenset([9])
    FOLLOW_COL_in_opener518 = frozenset([39])
    FOLLOW_STR_in_opener520 = frozenset([1])
    FOLLOW_BODYLBL_in_body527 = frozenset([9])
    FOLLOW_COL_in_body529 = frozenset([25])
    FOLLOW_OBR_in_body531 = frozenset([47])
    FOLLOW_effects_in_body533 = frozenset([4, 6])
    FOLLOW_AND_in_body536 = frozenset([15])
    FOLLOW_conditional_in_body538 = frozenset([4, 6])
    FOLLOW_CBR_in_body543 = frozenset([1])
    FOLLOW_BODYLBL_in_body548 = frozenset([9])
    FOLLOW_COL_in_body550 = frozenset([25])
    FOLLOW_OBR_in_body552 = frozenset([15])
    FOLLOW_conditional_in_body554 = frozenset([6, 12])
    FOLLOW_ELSE_in_body557 = frozenset([15])
    FOLLOW_conditional_in_body559 = frozenset([6, 12])
    FOLLOW_ELSE_in_body564 = frozenset([47])
    FOLLOW_effects_in_body566 = frozenset([6])
    FOLLOW_CBR_in_body570 = frozenset([1])
    FOLLOW_expr_in_effects577 = frozenset([1, 4])
    FOLLOW_AND_in_effects580 = frozenset([47])
    FOLLOW_expr_in_effects582 = frozenset([1, 4])
    FOLLOW_IF_in_conditional591 = frozenset([47])
    FOLLOW_expr_in_conditional593 = frozenset([4, 44])
    FOLLOW_AND_in_conditional596 = frozenset([47])
    FOLLOW_expr_in_conditional598 = frozenset([4, 44])
    FOLLOW_THEN_in_conditional602 = frozenset([47])
    FOLLOW_effects_in_conditional604 = frozenset([1])
    FOLLOW_VALUE_in_expr611 = frozenset([25])
    FOLLOW_OBR_in_expr613 = frozenset([47])
    FOLLOW_VALUE_in_expr615 = frozenset([6, 8])
    FOLLOW_CMA_in_expr618 = frozenset([47])
    FOLLOW_VALUE_in_expr620 = frozenset([6, 8])
    FOLLOW_CBR_in_expr624 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("dgdlLexer", dgdlParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
