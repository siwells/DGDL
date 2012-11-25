# $ANTLR 3.4 /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g 2012-11-23 11:29:38

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



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


class dgdlLexer(Lexer):

    grammarFileName = "/Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(dgdlLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )






    # $ANTLR start "COMPLBL"
    def mCOMPLBL(self, ):
        try:
            _type = COMPLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:35:9: ( 'composition' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:35:11: 'composition'
            pass 
            self.match("composition")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMPLBL"



    # $ANTLR start "CONTENTLBL"
    def mCONTENTLBL(self, ):
        try:
            _type = CONTENTLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:36:11: ( 'content' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:36:13: 'content'
            pass 
            self.match("content")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CONTENTLBL"



    # $ANTLR start "BODYLBL"
    def mBODYLBL(self, ):
        try:
            _type = BODYLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:37:9: ( 'body' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:37:11: 'body'
            pass 
            self.match("body")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BODYLBL"



    # $ANTLR start "MINLBL"
    def mMINLBL(self, ):
        try:
            _type = MINLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:38:8: ( 'min' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:38:10: 'min'
            pass 
            self.match("min")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MINLBL"



    # $ANTLR start "MAXLBL"
    def mMAXLBL(self, ):
        try:
            _type = MAXLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:39:8: ( 'max' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:39:10: 'max'
            pass 
            self.match("max")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MAXLBL"



    # $ANTLR start "TURNLBL"
    def mTURNLBL(self, ):
        try:
            _type = TURNLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:40:9: ( 'turns' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:40:11: 'turns'
            pass 
            self.match("turns")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TURNLBL"



    # $ANTLR start "MAGLBL"
    def mMAGLBL(self, ):
        try:
            _type = MAGLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:41:8: ( 'magnitude' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:41:10: 'magnitude'
            pass 
            self.match("magnitude")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MAGLBL"



    # $ANTLR start "MAG"
    def mMAG(self, ):
        try:
            _type = MAG
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:42:5: ( 'single' | 'multiple' )
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 115) :
                alt1 = 1
            elif (LA1_0 == 109) :
                alt1 = 2
            else:
                nvae = NoViableAltException("", 1, 0, self.input)

                raise nvae


            if alt1 == 1:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:42:7: 'single'
                pass 
                self.match("single")



            elif alt1 == 2:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:42:16: 'multiple'
                pass 
                self.match("multiple")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MAG"



    # $ANTLR start "MOVELBL"
    def mMOVELBL(self, ):
        try:
            _type = MOVELBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:43:9: ( 'move' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:43:11: 'move'
            pass 
            self.match("move")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MOVELBL"



    # $ANTLR start "MOVESLBL"
    def mMOVESLBL(self, ):
        try:
            _type = MOVESLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:44:10: ( 'moves' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:44:12: 'moves'
            pass 
            self.match("moves")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MOVESLBL"



    # $ANTLR start "ORDLBL"
    def mORDLBL(self, ):
        try:
            _type = ORDLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:45:8: ( 'ordering' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:45:10: 'ordering'
            pass 
            self.match("ordering")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ORDLBL"



    # $ANTLR start "ORD"
    def mORD(self, ):
        try:
            _type = ORD
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:46:5: ( 'strict' | 'liberal' )
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 115) :
                alt2 = 1
            elif (LA2_0 == 108) :
                alt2 = 2
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae


            if alt2 == 1:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:46:7: 'strict'
                pass 
                self.match("strict")



            elif alt2 == 2:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:46:16: 'liberal'
                pass 
                self.match("liberal")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ORD"



    # $ANTLR start "SCOPELBL"
    def mSCOPELBL(self, ):
        try:
            _type = SCOPELBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:47:10: ( 'scope' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:47:12: 'scope'
            pass 
            self.match("scope")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SCOPELBL"



    # $ANTLR start "SCOPEVAL"
    def mSCOPEVAL(self, ):
        try:
            _type = SCOPEVAL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:48:10: ( 'initial' | 'turnwise' | 'movewise' )
            alt3 = 3
            LA3 = self.input.LA(1)
            if LA3 == 105:
                alt3 = 1
            elif LA3 == 116:
                alt3 = 2
            elif LA3 == 109:
                alt3 = 3
            else:
                nvae = NoViableAltException("", 3, 0, self.input)

                raise nvae


            if alt3 == 1:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:48:12: 'initial'
                pass 
                self.match("initial")



            elif alt3 == 2:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:48:22: 'turnwise'
                pass 
                self.match("turnwise")



            elif alt3 == 3:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:48:33: 'movewise'
                pass 
                self.match("movewise")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SCOPEVAL"



    # $ANTLR start "STRUCTLBL"
    def mSTRUCTLBL(self, ):
        try:
            _type = STRUCTLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:49:11: ( 'structure' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:49:13: 'structure'
            pass 
            self.match("structure")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRUCTLBL"



    # $ANTLR start "STRUCTVAL"
    def mSTRUCTVAL(self, ):
        try:
            _type = STRUCTVAL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:50:11: ( 'set' | 'queue' | 'stack' )
            alt4 = 3
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 115) :
                LA4_1 = self.input.LA(2)

                if (LA4_1 == 101) :
                    alt4 = 1
                elif (LA4_1 == 116) :
                    alt4 = 3
                else:
                    nvae = NoViableAltException("", 4, 1, self.input)

                    raise nvae


            elif (LA4_0 == 113) :
                alt4 = 2
            else:
                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae


            if alt4 == 1:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:50:13: 'set'
                pass 
                self.match("set")



            elif alt4 == 2:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:50:19: 'queue'
                pass 
                self.match("queue")



            elif alt4 == 3:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:50:27: 'stack'
                pass 
                self.match("stack")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRUCTVAL"



    # $ANTLR start "VISLBL"
    def mVISLBL(self, ):
        try:
            _type = VISLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:51:8: ( 'visibility' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:51:10: 'visibility'
            pass 
            self.match("visibility")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VISLBL"



    # $ANTLR start "VISVAL"
    def mVISVAL(self, ):
        try:
            _type = VISVAL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:52:8: ( 'public' | 'private' )
            alt5 = 2
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 112) :
                LA5_1 = self.input.LA(2)

                if (LA5_1 == 117) :
                    alt5 = 1
                elif (LA5_1 == 114) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 1, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 5, 0, self.input)

                raise nvae


            if alt5 == 1:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:52:10: 'public'
                pass 
                self.match("public")



            elif alt5 == 2:
                # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:52:19: 'private'
                pass 
                self.match("private")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VISVAL"



    # $ANTLR start "OWNERLBL"
    def mOWNERLBL(self, ):
        try:
            _type = OWNERLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:53:10: ( 'owner' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:53:12: 'owner'
            pass 
            self.match("owner")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OWNERLBL"



    # $ANTLR start "PLAYERLBL"
    def mPLAYERLBL(self, ):
        try:
            _type = PLAYERLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:54:11: ( 'player' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:54:13: 'player'
            pass 
            self.match("player")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PLAYERLBL"



    # $ANTLR start "UNDEFLBL"
    def mUNDEFLBL(self, ):
        try:
            _type = UNDEFLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:55:10: ( 'undefined' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:55:12: 'undefined'
            pass 
            self.match("undefined")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UNDEFLBL"



    # $ANTLR start "PARTLBL"
    def mPARTLBL(self, ):
        try:
            _type = PARTLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:56:9: ( 'players' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:56:11: 'players'
            pass 
            self.match("players")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PARTLBL"



    # $ANTLR start "GAMELBL"
    def mGAMELBL(self, ):
        try:
            _type = GAMELBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:57:9: ( 'game' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:57:11: 'game'
            pass 
            self.match("game")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GAMELBL"



    # $ANTLR start "SYSLBL"
    def mSYSLBL(self, ):
        try:
            _type = SYSLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:58:8: ( 'system' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:58:10: 'system'
            pass 
            self.match("system")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SYSLBL"



    # $ANTLR start "OPENLBL"
    def mOPENLBL(self, ):
        try:
            _type = OPENLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:59:9: ( 'opener' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:59:11: 'opener'
            pass 
            self.match("opener")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OPENLBL"



    # $ANTLR start "ROLELBL"
    def mROLELBL(self, ):
        try:
            _type = ROLELBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:60:9: ( 'roles' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:60:11: 'roles'
            pass 
            self.match("roles")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ROLELBL"



    # $ANTLR start "RULELBL"
    def mRULELBL(self, ):
        try:
            _type = RULELBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:61:9: ( 'rule' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:61:11: 'rule'
            pass 
            self.match("rule")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RULELBL"



    # $ANTLR start "RULESLBL"
    def mRULESLBL(self, ):
        try:
            _type = RULESLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:62:10: ( 'rules' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:62:12: 'rules'
            pass 
            self.match("rules")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RULESLBL"



    # $ANTLR start "STORELBL"
    def mSTORELBL(self, ):
        try:
            _type = STORELBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:63:10: ( 'store' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:63:12: 'store'
            pass 
            self.match("store")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STORELBL"



    # $ANTLR start "AND"
    def mAND(self, ):
        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:64:5: ( 'and' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:64:7: 'and'
            pass 
            self.match("and")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AND"



    # $ANTLR start "IF"
    def mIF(self, ):
        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:65:4: ( 'if' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:65:6: 'if'
            pass 
            self.match("if")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IF"



    # $ANTLR start "THEN"
    def mTHEN(self, ):
        try:
            _type = THEN
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:66:6: ( 'then' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:66:8: 'then'
            pass 
            self.match("then")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "THEN"



    # $ANTLR start "ELSE"
    def mELSE(self, ):
        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:67:6: ( 'else' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:67:8: 'else'
            pass 
            self.match("else")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "NOT"
    def mNOT(self, ):
        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:68:5: ( '!' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:68:7: '!'
            pass 
            self.match(33)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOT"



    # $ANTLR start "IDLBL"
    def mIDLBL(self, ):
        try:
            _type = IDLBL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:69:7: ( 'id' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:69:9: 'id'
            pass 
            self.match("id")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IDLBL"



    # $ANTLR start "LINK"
    def mLINK(self, ):
        try:
            _type = LINK
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:70:6: ( '_' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:70:8: '_'
            pass 
            self.match(95)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LINK"



    # $ANTLR start "SYM"
    def mSYM(self, ):
        try:
            _type = SYM
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:71:5: ( '?' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:71:7: '?'
            pass 
            self.match(63)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SYM"



    # $ANTLR start "OBR"
    def mOBR(self, ):
        try:
            _type = OBR
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:72:5: ( '{' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:72:7: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OBR"



    # $ANTLR start "CBR"
    def mCBR(self, ):
        try:
            _type = CBR
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:73:5: ( '}' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:73:7: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CBR"



    # $ANTLR start "CMA"
    def mCMA(self, ):
        try:
            _type = CMA
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:74:5: ( ',' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:74:7: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CMA"



    # $ANTLR start "COL"
    def mCOL(self, ):
        try:
            _type = COL
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:75:5: ( ':' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:75:7: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COL"



    # $ANTLR start "STAR"
    def mSTAR(self, ):
        try:
            _type = STAR
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:76:6: ( '*' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:76:8: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STAR"



    # $ANTLR start "STR"
    def mSTR(self, ):
        try:
            _type = STR
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:77:5: ( '\"' ( CHAR | WS )+ '\"' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:77:7: '\"' ( CHAR | WS )+ '\"'
            pass 
            self.match(34)

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:77:10: ( CHAR | WS )+
            cnt6 = 0
            while True: #loop6
                alt6 = 3
                LA6_0 = self.input.LA(1)

                if ((65 <= LA6_0 <= 90) or (97 <= LA6_0 <= 122)) :
                    alt6 = 1
                elif ((9 <= LA6_0 <= 10) or LA6_0 == 13 or LA6_0 == 32) :
                    alt6 = 2


                if alt6 == 1:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:77:11: CHAR
                    pass 
                    self.mCHAR()



                elif alt6 == 2:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:77:16: WS
                    pass 
                    self.mWS()



                else:
                    if cnt6 >= 1:
                        break #loop6

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1


            self.match(34)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STR"



    # $ANTLR start "VALUE"
    def mVALUE(self, ):
        try:
            _type = VALUE
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:78:7: ( CHAR ( CHAR | LINK | NUM | STAR )+ )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:78:9: CHAR ( CHAR | LINK | NUM | STAR )+
            pass 
            self.mCHAR()


            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:78:13: ( CHAR | LINK | NUM | STAR )+
            cnt7 = 0
            while True: #loop7
                alt7 = 5
                LA7 = self.input.LA(1)
                if LA7 == 65 or LA7 == 66 or LA7 == 67 or LA7 == 68 or LA7 == 69 or LA7 == 70 or LA7 == 71 or LA7 == 72 or LA7 == 73 or LA7 == 74 or LA7 == 75 or LA7 == 76 or LA7 == 77 or LA7 == 78 or LA7 == 79 or LA7 == 80 or LA7 == 81 or LA7 == 82 or LA7 == 83 or LA7 == 84 or LA7 == 85 or LA7 == 86 or LA7 == 87 or LA7 == 88 or LA7 == 89 or LA7 == 90 or LA7 == 97 or LA7 == 98 or LA7 == 99 or LA7 == 100 or LA7 == 101 or LA7 == 102 or LA7 == 103 or LA7 == 104 or LA7 == 105 or LA7 == 106 or LA7 == 107 or LA7 == 108 or LA7 == 109 or LA7 == 110 or LA7 == 111 or LA7 == 112 or LA7 == 113 or LA7 == 114 or LA7 == 115 or LA7 == 116 or LA7 == 117 or LA7 == 118 or LA7 == 119 or LA7 == 120 or LA7 == 121 or LA7 == 122:
                    alt7 = 1
                elif LA7 == 95:
                    alt7 = 2
                elif LA7 == 48 or LA7 == 49 or LA7 == 50 or LA7 == 51 or LA7 == 52 or LA7 == 53 or LA7 == 54 or LA7 == 55 or LA7 == 56 or LA7 == 57:
                    alt7 = 3
                elif LA7 == 42:
                    alt7 = 4

                if alt7 == 1:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:78:14: CHAR
                    pass 
                    self.mCHAR()



                elif alt7 == 2:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:78:19: LINK
                    pass 
                    self.mLINK()



                elif alt7 == 3:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:78:24: NUM
                    pass 
                    self.mNUM()



                elif alt7 == 4:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:78:28: STAR
                    pass 
                    self.mSTAR()



                else:
                    if cnt7 >= 1:
                        break #loop7

                    eee = EarlyExitException(7, self.input)
                    raise eee

                cnt7 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VALUE"



    # $ANTLR start "CHAR"
    def mCHAR(self, ):
        try:
            _type = CHAR
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:79:6: ( 'a' .. 'z' | 'A' .. 'Z' )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CHAR"



    # $ANTLR start "NUM"
    def mNUM(self, ):
        try:
            _type = NUM
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:80:5: ( ( '0' .. '9' )+ )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:80:7: ( '0' .. '9' )+
            pass 
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:80:7: ( '0' .. '9' )+
            cnt8 = 0
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((48 <= LA8_0 <= 57)) :
                    alt8 = 1


                if alt8 == 1:
                    # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt8 >= 1:
                        break #loop8

                    eee = EarlyExitException(8, self.input)
                    raise eee

                cnt8 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NUM"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:81:6: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:81:8: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:8: ( COMPLBL | CONTENTLBL | BODYLBL | MINLBL | MAXLBL | TURNLBL | MAGLBL | MAG | MOVELBL | MOVESLBL | ORDLBL | ORD | SCOPELBL | SCOPEVAL | STRUCTLBL | STRUCTVAL | VISLBL | VISVAL | OWNERLBL | PLAYERLBL | UNDEFLBL | PARTLBL | GAMELBL | SYSLBL | OPENLBL | ROLELBL | RULELBL | RULESLBL | STORELBL | AND | IF | THEN | ELSE | NOT | IDLBL | LINK | SYM | OBR | CBR | CMA | COL | STAR | STR | VALUE | CHAR | NUM | WS )
        alt9 = 47
        alt9 = self.dfa9.predict(self.input)
        if alt9 == 1:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:10: COMPLBL
            pass 
            self.mCOMPLBL()



        elif alt9 == 2:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:18: CONTENTLBL
            pass 
            self.mCONTENTLBL()



        elif alt9 == 3:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:29: BODYLBL
            pass 
            self.mBODYLBL()



        elif alt9 == 4:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:37: MINLBL
            pass 
            self.mMINLBL()



        elif alt9 == 5:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:44: MAXLBL
            pass 
            self.mMAXLBL()



        elif alt9 == 6:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:51: TURNLBL
            pass 
            self.mTURNLBL()



        elif alt9 == 7:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:59: MAGLBL
            pass 
            self.mMAGLBL()



        elif alt9 == 8:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:66: MAG
            pass 
            self.mMAG()



        elif alt9 == 9:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:70: MOVELBL
            pass 
            self.mMOVELBL()



        elif alt9 == 10:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:78: MOVESLBL
            pass 
            self.mMOVESLBL()



        elif alt9 == 11:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:87: ORDLBL
            pass 
            self.mORDLBL()



        elif alt9 == 12:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:94: ORD
            pass 
            self.mORD()



        elif alt9 == 13:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:98: SCOPELBL
            pass 
            self.mSCOPELBL()



        elif alt9 == 14:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:107: SCOPEVAL
            pass 
            self.mSCOPEVAL()



        elif alt9 == 15:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:116: STRUCTLBL
            pass 
            self.mSTRUCTLBL()



        elif alt9 == 16:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:126: STRUCTVAL
            pass 
            self.mSTRUCTVAL()



        elif alt9 == 17:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:136: VISLBL
            pass 
            self.mVISLBL()



        elif alt9 == 18:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:143: VISVAL
            pass 
            self.mVISVAL()



        elif alt9 == 19:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:150: OWNERLBL
            pass 
            self.mOWNERLBL()



        elif alt9 == 20:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:159: PLAYERLBL
            pass 
            self.mPLAYERLBL()



        elif alt9 == 21:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:169: UNDEFLBL
            pass 
            self.mUNDEFLBL()



        elif alt9 == 22:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:178: PARTLBL
            pass 
            self.mPARTLBL()



        elif alt9 == 23:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:186: GAMELBL
            pass 
            self.mGAMELBL()



        elif alt9 == 24:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:194: SYSLBL
            pass 
            self.mSYSLBL()



        elif alt9 == 25:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:201: OPENLBL
            pass 
            self.mOPENLBL()



        elif alt9 == 26:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:209: ROLELBL
            pass 
            self.mROLELBL()



        elif alt9 == 27:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:217: RULELBL
            pass 
            self.mRULELBL()



        elif alt9 == 28:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:225: RULESLBL
            pass 
            self.mRULESLBL()



        elif alt9 == 29:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:234: STORELBL
            pass 
            self.mSTORELBL()



        elif alt9 == 30:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:243: AND
            pass 
            self.mAND()



        elif alt9 == 31:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:247: IF
            pass 
            self.mIF()



        elif alt9 == 32:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:250: THEN
            pass 
            self.mTHEN()



        elif alt9 == 33:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:255: ELSE
            pass 
            self.mELSE()



        elif alt9 == 34:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:260: NOT
            pass 
            self.mNOT()



        elif alt9 == 35:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:264: IDLBL
            pass 
            self.mIDLBL()



        elif alt9 == 36:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:270: LINK
            pass 
            self.mLINK()



        elif alt9 == 37:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:275: SYM
            pass 
            self.mSYM()



        elif alt9 == 38:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:279: OBR
            pass 
            self.mOBR()



        elif alt9 == 39:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:283: CBR
            pass 
            self.mCBR()



        elif alt9 == 40:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:287: CMA
            pass 
            self.mCMA()



        elif alt9 == 41:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:291: COL
            pass 
            self.mCOL()



        elif alt9 == 42:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:295: STAR
            pass 
            self.mSTAR()



        elif alt9 == 43:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:300: STR
            pass 
            self.mSTR()



        elif alt9 == 44:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:304: VALUE
            pass 
            self.mVALUE()



        elif alt9 == 45:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:310: CHAR
            pass 
            self.mCHAR()



        elif alt9 == 46:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:315: NUM
            pass 
            self.mNUM()



        elif alt9 == 47:
            # /Users/siwells/Documents/projects/moot/dgdl/dev/dgdl.g:1:319: WS
            pass 
            self.mWS()








    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\1\uffff\20\36\11\uffff\1\36\2\uffff\1\37\2\uffff\21\37\1\124\1"
        u"\125\16\37\1\144\1\145\12\37\1\161\6\37\2\uffff\11\37\1\u0081\3"
        u"\37\1\u0085\2\uffff\2\37\1\u008a\1\37\1\u008d\6\37\1\uffff\14\37"
        u"\1\u00a0\1\37\1\u00a3\1\uffff\1\u00a4\2\37\1\uffff\2\37\1\u00a9"
        u"\1\37\1\uffff\1\u00ab\1\37\1\uffff\3\37\1\161\1\u00b0\1\u00b1\2"
        u"\37\1\u00b4\3\37\1\161\5\37\1\uffff\1\u00bd\1\u00be\2\uffff\4\37"
        u"\1\uffff\1\37\1\uffff\1\37\1\u00c5\1\u00c6\1\37\2\uffff\1\u00c8"
        u"\1\37\1\uffff\1\u00ca\3\37\1\u00ce\1\37\1\u00d1\1\37\2\uffff\1"
        u"\37\1\u00d4\4\37\2\uffff\1\37\1\uffff\1\37\1\uffff\1\u00c6\1\u00db"
        u"\1\37\1\uffff\1\u00ce\1\u00dd\1\uffff\2\37\1\uffff\1\37\1\u00c5"
        u"\2\u00db\1\37\1\u00e2\1\uffff\1\37\1\uffff\2\37\1\u00e6\1\u00e7"
        u"\1\uffff\1\37\1\u00e9\1\37\2\uffff\1\u00eb\1\uffff\1\u00ec\2\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\u00ed\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\11\20\52\11\uffff\1\52\2\uffff\1\155\2\uffff\1\144\1\156\1\147"
        u"\1\154\1\166\1\162\1\145\1\156\1\141\1\157\1\164\1\163\1\144\1"
        u"\156\1\145\1\142\1\151\2\52\1\145\1\163\1\142\1\151\1\141\1\144"
        u"\1\155\2\154\1\144\1\163\1\160\1\164\1\171\2\52\1\156\1\164\1\145"
        u"\2\156\1\147\1\151\1\143\1\162\1\160\1\52\1\164\2\145\1\156\1\145"
        u"\1\164\2\uffff\1\165\1\151\1\154\1\166\1\171\4\145\1\52\1\145\1"
        u"\157\1\145\1\52\2\uffff\2\151\1\52\1\163\1\52\1\154\2\143\1\153"
        u"\2\145\1\uffff\1\145\2\162\1\145\1\162\1\151\1\145\1\142\1\151"
        u"\1\141\1\145\1\146\1\52\1\163\1\52\1\uffff\1\52\1\163\1\156\1\uffff"
        u"\1\164\1\160\1\52\1\151\1\uffff\1\52\1\151\1\uffff\1\145\2\164"
        u"\3\52\1\155\1\151\1\52\1\162\2\141\1\52\1\151\1\143\1\164\1\162"
        u"\1\151\1\uffff\2\52\2\uffff\1\151\1\164\1\165\1\154\1\uffff\1\163"
        u"\1\uffff\1\163\2\52\1\165\2\uffff\1\52\1\156\1\uffff\1\52\3\154"
        u"\1\52\1\145\1\52\1\156\2\uffff\1\164\1\52\1\144\3\145\2\uffff\1"
        u"\162\1\uffff\1\147\1\uffff\2\52\1\151\1\uffff\2\52\1\uffff\1\145"
        u"\1\151\1\uffff\1\145\3\52\1\145\1\52\1\uffff\1\164\1\uffff\1\144"
        u"\1\157\2\52\1\uffff\1\171\1\52\1\156\2\uffff\1\52\1\uffff\1\52"
        u"\2\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\1\175\20\172\11\uffff\1\172\2\uffff\1\156\2\uffff\1\144\1\156"
        u"\1\170\1\154\1\166\1\162\1\145\1\156\1\162\1\157\1\164\1\163\1"
        u"\144\1\156\1\145\1\142\1\151\2\172\1\145\1\163\1\142\1\151\1\141"
        u"\1\144\1\155\2\154\1\144\1\163\1\160\1\164\1\171\2\172\1\156\1"
        u"\164\1\145\2\156\1\147\1\165\1\143\1\162\1\160\1\172\1\164\2\145"
        u"\1\156\1\145\1\164\2\uffff\1\165\1\151\1\154\1\166\1\171\4\145"
        u"\1\172\1\145\1\157\1\145\1\172\2\uffff\2\151\1\172\1\167\1\172"
        u"\1\154\2\143\1\153\2\145\1\uffff\1\145\2\162\1\145\1\162\1\151"
        u"\1\145\1\142\1\151\1\141\1\145\1\146\1\172\1\163\1\172\1\uffff"
        u"\1\172\1\163\1\156\1\uffff\1\164\1\160\1\172\1\151\1\uffff\1\172"
        u"\1\151\1\uffff\1\145\2\164\3\172\1\155\1\151\1\172\1\162\2\141"
        u"\1\172\1\151\1\143\1\164\1\162\1\151\1\uffff\2\172\2\uffff\1\151"
        u"\1\164\1\165\1\154\1\uffff\1\163\1\uffff\1\163\2\172\1\165\2\uffff"
        u"\1\172\1\156\1\uffff\1\172\3\154\1\172\1\145\1\172\1\156\2\uffff"
        u"\1\164\1\172\1\144\3\145\2\uffff\1\162\1\uffff\1\147\1\uffff\2"
        u"\172\1\151\1\uffff\2\172\1\uffff\1\145\1\151\1\uffff\1\145\3\172"
        u"\1\145\1\172\1\uffff\1\164\1\uffff\1\144\1\157\2\172\1\uffff\1"
        u"\171\1\172\1\156\2\uffff\1\172\1\uffff\1\172\2\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\21\uffff\1\42\1\44\1\45\1\46\1\47\1\50\1\51\1\52\1\53\1\uffff"
        u"\1\56\1\57\1\uffff\1\55\1\54\64\uffff\1\37\1\43\16\uffff\1\4\1"
        u"\5\13\uffff\1\20\17\uffff\1\36\3\uffff\1\3\4\uffff\1\11\2\uffff"
        u"\1\40\22\uffff\1\27\2\uffff\1\33\1\41\4\uffff\1\12\1\uffff\1\6"
        u"\4\uffff\1\35\1\15\2\uffff\1\23\10\uffff\1\32\1\34\6\uffff\1\10"
        u"\1\14\1\uffff\1\30\1\uffff\1\31\3\uffff\1\22\2\uffff\1\24\2\uffff"
        u"\1\2\6\uffff\1\16\1\uffff\1\26\4\uffff\1\13\3\uffff\1\7\1\17\1"
        u"\uffff\1\25\1\uffff\1\21\1\1"
        )

    DFA9_special = DFA.unpack(
        u"\u00ed\uffff"
        )


    DFA9_transition = [
        DFA.unpack(u"\2\34\2\uffff\1\34\22\uffff\1\34\1\21\1\31\7\uffff\1"
        u"\30\1\uffff\1\26\3\uffff\12\33\1\27\4\uffff\1\23\1\uffff\32\32"
        u"\4\uffff\1\22\1\uffff\1\17\1\2\1\1\1\32\1\20\1\32\1\15\1\32\1\10"
        u"\2\32\1\7\1\3\1\32\1\6\1\13\1\11\1\16\1\5\1\4\1\14\1\12\4\32\1"
        u"\24\1\uffff\1\25"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\16\37\1\35\13\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\16\37\1\40\13\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\1\42\7\37\1\41\5\37\1\44\5\37\1\43\5\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\7\37\1\46\14\37\1\45\5\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\2\37\1\51\1\37\1\52\3\37\1\47\12\37\1\50\4\37\1\53\1\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\17\37\1\56\1\37\1\54\4\37\1\55\3\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\10\37\1\57\21\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\3\37\1\62\1\37\1\61\7\37\1\60\14\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\24\37\1\63\5\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\10\37\1\64\21\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\13\37\1\67\5\37\1\66\2\37\1\65\5\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\15\37\1\70\14\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\1\71\31\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\16\37\1\72\5\37\1\73\5\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\15\37\1\74\14\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\13\37\1\75\16\37"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\76\1\77"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\103\20\uffff\1\102"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\112\15\uffff\1\113\2\uffff\1\111"),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u"\1\120"),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\1\151"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\1\154\13\uffff\1\155"),
        DFA.unpack(u"\1\156"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u"\1\164"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\1\166"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\172"),
        DFA.unpack(u"\1\173"),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\1\177"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u"\1\u0084"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\22\37\1\u0088\3\37\1\u0089\3\37"),
        DFA.unpack(u"\1\u008b\3\uffff\1\u008c"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\1\u0090"),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u"\1\u0092"),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0094"),
        DFA.unpack(u"\1\u0095"),
        DFA.unpack(u"\1\u0096"),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u"\1\u0099"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u"\1\u009b"),
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u"\1\u009d"),
        DFA.unpack(u"\1\u009e"),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00a1"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\22\37\1\u00a2\7\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00a5"),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u"\1\u00a8"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00ac"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ad"),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00b2"),
        DFA.unpack(u"\1\u00b3"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u"\1\u00b7"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00b8"),
        DFA.unpack(u"\1\u00b9"),
        DFA.unpack(u"\1\u00ba"),
        DFA.unpack(u"\1\u00bb"),
        DFA.unpack(u"\1\u00bc"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00bf"),
        DFA.unpack(u"\1\u00c0"),
        DFA.unpack(u"\1\u00c1"),
        DFA.unpack(u"\1\u00c2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00c3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00c4"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00c7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00c9"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00cb"),
        DFA.unpack(u"\1\u00cc"),
        DFA.unpack(u"\1\u00cd"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00cf"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\22\37\1\u00d0\7\37"),
        DFA.unpack(u"\1\u00d2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d3"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00d5"),
        DFA.unpack(u"\1\u00d6"),
        DFA.unpack(u"\1\u00d7"),
        DFA.unpack(u"\1\u00d8"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d9"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00da"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00dc"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00de"),
        DFA.unpack(u"\1\u00df"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e0"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00e1"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e4"),
        DFA.unpack(u"\1\u00e5"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e8"),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u"\1\u00ea"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\5\uffff\12\37\7\uffff\32\37\4\uffff\1\37\1\uffff"
        u"\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(dgdlLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
